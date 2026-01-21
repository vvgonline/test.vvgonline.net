// src/wwwroot/assets/js/chat.js

window.transformersChat = {
    model: null,
    dotnetHelper: null,

    async init(dotnetHelper) {
        this.dotnetHelper = dotnetHelper;
        try {
            const { pipeline, env } = await import('https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.0.0');

            // Critical Environment Configuration
            env.allowLocalModels = true;
            env.allowRemoteModels = false;
            env.localModelPath = '/model-repo/';
            env.useBrowserCache = false; // Prevents loading the corrupted HTML from cache

            console.log("Starting pipeline initialization...");

            this.model = await pipeline('text-generation', 'nuriyev/Qwen2.5-0.5B-Instruct-medical-dpo-onnx', {
                progress_callback: (p) => {
                    console.log('Loading:', p.file, p.status);
                    this.dotnetHelper.invokeMethodAsync('UpdateProgress', `Loading ${p.file}...`);
                }
            });

            console.log("SUCCESS: Model assigned to this.model", this.model);
            await this.dotnetHelper.invokeMethodAsync('OnModelReady');

        } catch (error) {
            console.error("FATAL INIT ERROR:", error);
            await this.dotnetHelper.invokeMethodAsync('UpdateProgress', `Init Error: ${error.message}`);
        }
    },

    async generate(messages) {
        if (!this.model) {
            console.error('Model not initialized.');
            return 'Error: Model not ready.';
        }

        try {
            // Convert chat history to single prompt
            const prompt = this.formatMessages(messages);

            const result = await this.model(prompt, {
                max_new_tokens: 150,
                temperature: 0.7,
                top_k: 50,
                do_sample: true
            });

            // Extract just the new generated text (not the whole prompt)
            const generated = result[0].generated_text;
            const response = generated.substring(prompt.length).trim();

            return response;

        } catch (error) {
            console.error('Text generation failed:', error);
            return `Error: ${error.message}`;
        }
    },

    formatMessages(messages) {
        // Convert message array to LLM chat format
        let prompt = '';

        for (const msg of messages) {
            if (msg.role === 'system') {
                prompt += `System: ${msg.content}\n\n`;
            } else if (msg.role === 'user') {
                prompt += `User: ${msg.content}\n`;
            } else if (msg.role === 'assistant') {
                prompt += `Assistant: ${msg.content}\n`;
            }
        }

        prompt += 'Assistant:';
        return prompt;
    }
};
