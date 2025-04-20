#!/usr/bin/env python3
import os
import json
import anthropic
from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass

@dataclass
class ModelResponse:
    """Represents a response from a language model."""
    content: str
    confidence: float
    model_name: str
    tokens_used: int

@dataclass
class CodeGeneration:
    """Represents generated code with metadata."""
    code: str
    explanation: str
    references: List[str]
    confidence: float

class ModelManager:
    """Manages interactions with various language models for code understanding and generation."""
    
    def __init__(self, api_keys: Dict[str, str] = None):
        self.api_keys = api_keys or {}
        self.models = self._initialize_models()
        self.context_window = {}
        self.response_cache = {}
        
    def _initialize_models(self) -> Dict[str, Any]:
        """Initialize connections to various language models."""
        models = {}
        
        # Initialize Anthropic client if API key is available
        if 'anthropic' in self.api_keys:
            models['anthropic'] = anthropic.Anthropic(api_key=self.api_keys['anthropic'])
            
        # Add support for local models via Ollama if available
        ollama_model = os.environ.get("AGER_OLLAMA_MODEL")
        if ollama_model:
            models['ollama'] = {'model_name': ollama_model}
            
        return models
    
    async def generate_code(self, prompt: str, context: Dict[str, Any], model_preference: str = None) -> CodeGeneration:
        """Generate code based on prompt and context using the most appropriate model."""
        # Select the best model based on task requirements and availability
        model = self._select_model(model_preference)
        
        # Prepare the prompt with context
        enhanced_prompt = self._enhance_prompt(prompt, context)
        
        # Generate code using the selected model
        if model == 'anthropic':
            response = await self._generate_with_anthropic(enhanced_prompt)
        elif model == 'ollama':
            response = await self._generate_with_ollama(enhanced_prompt)
        else:
            raise ValueError(f"Unsupported model: {model}")
            
        # Parse and validate the generated code
        return self._parse_code_generation(response)
    
    def _enhance_prompt(self, prompt: str, context: Dict[str, Any]) -> str:
        """Enhance the prompt with relevant context and examples."""
        context_str = json.dumps(context, indent=2)
        return f"""Given the following context and requirements, generate appropriate code:

Context:
{context_str}

Requirements:
{prompt}

Please provide:
1. The implementation code
2. A brief explanation
3. Any relevant references or documentation
"""
    
    async def _generate_with_anthropic(self, prompt: str) -> ModelResponse:
        """Generate code using Anthropic's Claude model."""
        if 'anthropic' not in self.models:
            raise ValueError("Anthropic API key not configured")
            
        client = self.models['anthropic']
        response = await client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return ModelResponse(
            content=response.content[0].text,
            confidence=0.9,  # Claude typically provides high-quality responses
            model_name="claude-3-opus",
            tokens_used=response.usage.output_tokens
        )
    
    async def _generate_with_ollama(self, prompt: str) -> ModelResponse:
        """Generate code using local Ollama model."""
        if 'ollama' not in self.models:
            raise ValueError("Ollama model not configured")
            
        # Implementation would depend on Ollama's API
        # This is a placeholder for the actual implementation
        return ModelResponse(
            content="",
            confidence=0.7,
            model_name=self.models['ollama']['model_name'],
            tokens_used=0
        )
    
    def _select_model(self, preference: str = None) -> str:
        """Select the most appropriate model based on availability and requirements."""
        if preference and preference in self.models:
            return preference
            
        # Prefer Claude for complex tasks
        if 'anthropic' in self.models:
            return 'anthropic'
            
        # Fall back to Ollama if available
        if 'ollama' in self.models:
            return 'ollama'
            
        raise ValueError("No suitable model available")
    
    def _parse_code_generation(self, response: ModelResponse) -> CodeGeneration:
        """Parse the model response into structured code generation."""
        # This would be enhanced with better parsing logic
        content = response.content
        
        # Simple parsing - assume code is between triple backticks
        code_parts = content.split('```')
        if len(code_parts) >= 3:
            code = code_parts[1].strip()
            explanation = code_parts[0].strip()
        else:
            code = content
            explanation = ""
        
        return CodeGeneration(
            code=code,
            explanation=explanation,
            references=[],  # Would be enhanced to extract actual references
            confidence=response.confidence
        )
    
    def update_context_window(self, context: Dict[str, Any]):
        """Update the context window with new information."""
        self.context_window.update(context)
        
        # Maintain context window size to prevent token limit issues
        if len(json.dumps(self.context_window)) > 4000:  # Arbitrary limit
            # Remove oldest entries
            oldest_keys = list(self.context_window.keys())[:-10]  # Keep last 10 entries
            for key in oldest_keys:
                del self.context_window[key]