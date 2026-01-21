// src/wwwroot/assets/js/chat.js - ONNX Runtime Web with HuggingFace CDN

window.transformersChat = {
    session: null,
    tokenizer: null,
    dotnetHelper: null,
    modelConfig: null,

    async init(dotnetHelper) {
        this.dotnetHelper = dotnetHelper;
        try {
            await this.loadOnnxRuntime();
            console.log("ONNX Runtime loaded");

            await this.dotnetHelper.invokeMethodAsync('UpdateProgress', '// Downloading model from HuggingFace...');
            await this.loadModelConfig();

            await this.dotnetHelper.invokeMethodAsync('UpdateProgress', '// Loading tokenizer...');
            await this.loadTokenizer();

            await this.dotnetHelper.invokeMethodAsync('UpdateProgress', '// Loading AI model...');
            await this.loadModel();

            console.log("Model ready");
            await this.dotnetHelper.invokeMethodAsync('OnModelReady');

        } catch (error) {
            console.error("INIT ERROR:", error);
            await this.dotnetHelper.invokeMethodAsync('UpdateProgress', `// Error: ${error.message}`);
        }
    },

    async loadOnnxRuntime() {
        if (typeof ort === 'undefined') {
            return new Promise((resolve, reject) => {
                const script = document.createElement('script');
                script.src = 'https://cdn.jsdelivr.net/npm/onnxruntime-web@1.19.2/dist/ort.min.js';
                script.onload = () => {
                    console.log('ONNX Runtime loaded');
                    ort.env.wasm.wasmPaths = 'https://cdn.jsdelivr.net/npm/onnxruntime-web@1.19.2/dist/';
                    ort.env.wasm.numThreads = 1;
                    resolve();
                };
                script.onerror = () => reject(new Error('Failed to load ONNX Runtime'));
                document.head.appendChild(script);
            });
        }
    },

    async loadModelConfig() {
        try {
            // Load config from HuggingFace
            const configUrl = 'https://huggingface.co/Xenova/all-MiniLM-L6-v2/resolve/main/config.json';
            const response = await fetch(configUrl);

            if (response.ok) {
                this.modelConfig = await response.json();
                console.log('Config loaded:', this.modelConfig.model_type);
            } else {
                throw new Error('Config download failed');
            }
        } catch (error) {
            console.warn('Using default config:', error.message);
            // Default config for all-MiniLM-L6-v2
            this.modelConfig = {
                model_type: "bert",
                hidden_size: 384,
                num_hidden_layers: 6,
                num_attention_heads: 12,
                vocab_size: 30522,
                max_position_embeddings: 512
            };
        }
    },

    async loadTokenizer() {
        try {
            // Load tokenizer from HuggingFace
            const tokenizerUrl = 'https://huggingface.co/Xenova/all-MiniLM-L6-v2/resolve/main/tokenizer.json';
            const response = await fetch(tokenizerUrl);

            if (!response.ok) {
                throw new Error('Tokenizer download failed');
            }

            const tokenizerData = await response.json();
            console.log('Tokenizer downloaded');

            // Build vocab
            const vocab = {};
            const reverseVocab = {};

            if (tokenizerData.model && tokenizerData.model.vocab) {
                Object.assign(vocab, tokenizerData.model.vocab);
                for (let [token, id] of Object.entries(vocab)) {
                    reverseVocab[id] = token;
                }
            }

            console.log('Vocab size:', Object.keys(vocab).length);

            this.tokenizer = {
                vocab: vocab,
                reverseVocab: reverseVocab,
                vocabSize: Object.keys(vocab).length,

                encode: (text) => {
                    // Simple word-piece tokenization
                    const tokens = [101]; // [CLS] token

                    // Lowercase and split
                    const words = text.toLowerCase().split(/\s+/);

                    for (let word of words) {
                        // Try whole word first
                        if (vocab[word] !== undefined) {
                            tokens.push(vocab[word]);
                        } else {
                            // Try with ## prefix (subword)
                            let found = false;
                            for (let i = word.length; i > 0; i--) {
                                const subword = word.substring(0, i);
                                const key = i === word.length ? subword : '##' + subword;
                                if (vocab[key] !== undefined) {
                                    tokens.push(vocab[key]);
                                    found = true;

                                    // Continue with rest of word
                                    if (i < word.length) {
                                        const rest = word.substring(i);
                                        if (vocab['##' + rest] !== undefined) {
                                            tokens.push(vocab['##' + rest]);
                                        }
                                    }
                                    break;
                                }
                            }

                            if (!found) {
                                tokens.push(vocab['[UNK]'] || 100); // UNK token
                            }
                        }
                    }

                    tokens.push(102); // [SEP] token
                    return tokens;
                },

                decode: (tokenIds) => {
                    const tokens = tokenIds.map(id => {
                        if (id === 101) return '[CLS]';
                        if (id === 102) return '[SEP]';
                        if (id === 0) return '[PAD]';

                        const token = reverseVocab[id];
                        if (token) {
                            return token.replace('##', '');
                        }
                        return '[UNK]';
                    });
                    return tokens.join(' ').replace(/\s+/g, ' ').trim();
                }
            };

            console.log('Tokenizer ready');

        } catch (error) {
            console.warn('Tokenizer load failed:', error.message);
            this.tokenizer = this.createSimpleTokenizer();
        }
    },

    createSimpleTokenizer() {
        return {
            vocab: {},
            reverseVocab: {},
            vocabSize: 30522,
            encode: (text) => {
                // Very basic fallback
                const tokens = [101]; // CLS
                for (let char of text.toLowerCase()) {
                    tokens.push(char.charCodeAt(0) % 30000);
                }
                tokens.push(102); // SEP
                return tokens;
            },
            decode: (tokens) => {
                return tokens.map(t => String.fromCharCode(t)).join('');
            }
        };
    },

    async loadModel() {
        try {
            // Download ONNX model from HuggingFace
            const modelUrl = 'https://huggingface.co/Xenova/all-MiniLM-L6-v2/resolve/main/onnx/model_quantized.onnx';

            console.log('Downloading model from HuggingFace...');
            console.log('This may take a few moments (model size ~23MB)...');

            this.session = await ort.InferenceSession.create(modelUrl, {
                executionProviders: ['wasm'],
                graphOptimizationLevel: 'all',
                enableMemPattern: true,
                enableCpuMemArena: true,
            });

            console.log('Model loaded successfully');
            console.log('Model inputs:', this.session.inputNames);
            console.log('Model outputs:', this.session.outputNames);

        } catch (error) {
            console.error('Model download failed:', error);
            throw new Error(`Model loading failed: ${error.message}`);
        }
    },

    async generate(messages) {
        if (!this.session) {
            return '// Error: Model not initialized';
        }

        try {
            // Get user's last question
            const userMessage = messages.filter(m => m.role === 'user').pop();
            if (!userMessage) {
                return "Hello! How can I help you with VVG Online services?";
            }

            const userQuestion = userMessage.content;
            console.log('Processing question:', userQuestion);

            // Get context from system message
            const systemMessage = messages.find(m => m.role === 'system');
            const context = systemMessage ? systemMessage.content : '';

            // Simple keyword-based response (embedding model doesn't generate text)
            // For text generation, we'd need a different model
            const response = this.generateKeywordResponse(userQuestion, context);

            return response;

        } catch (error) {
            console.error('Generation error:', error);
            return `I'm here to help with VVG Online services. What would you like to know about web development, digital marketing, or business consulting?`;
        }
    },

    generateKeywordResponse(question, context) {
        const lowerQ = question.toLowerCase();
        const lowerContext = context.toLowerCase();

        // Search context for relevant information
        const lines = context.split('\n');
        const relevantLines = [];

        // Extract lines containing question keywords
        const keywords = question.toLowerCase().split(' ').filter(w => w.length > 3);

        for (const line of lines) {
            const lowerLine = line.toLowerCase();
            for (const keyword of keywords) {
                if (lowerLine.includes(keyword)) {
                    relevantLines.push(line.trim());
                    break;
                }
            }
        }

        // If we found relevant context, use it
        if (relevantLines.length > 0) {
            const response = relevantLines.slice(0, 5).join('\n');
            return response || this.getDefaultResponse(lowerQ);
        }

        // Fallback to keyword matching
        return this.getDefaultResponse(lowerQ);
    },

    getDefaultResponse(lowerQ) {
        if (lowerQ.includes('web') || lowerQ.includes('website') || lowerQ.includes('development')) {
            return "VVG Online specializes in web development including Blazor WebAssembly, ASP.NET Core, responsive design, and e-commerce solutions. We use modern technologies to build fast, scalable applications.";
        }

        if (lowerQ.includes('marketing') || lowerQ.includes('digital') || lowerQ.includes('seo')) {
            return "Our digital marketing services include SEO optimization, social media marketing, content strategy, and analytics. We create data-driven campaigns for measurable results.";
        }

        if (lowerQ.includes('contact') || lowerQ.includes('phone') || lowerQ.includes('reach')) {
            return "Contact VVG Online:\n📞 Phone: +91 9893261959\n🌐 Website: https://vvgonline.net\n📍 Location: Indore, India";
        }

        if (lowerQ.includes('price') || lowerQ.includes('cost') || lowerQ.includes('quote')) {
            return "We provide custom pricing based on your project requirements. Contact us at +91 9893261959 for a detailed quote.";
        }

        return "I can help you with VVG Online services:\n✓ Web Development\n✓ Digital Marketing\n✓ Business Consulting\n\nWhat would you like to know?";
    },

    formatMessages(messages) {
        let prompt = '';
        for (const msg of messages) {
            if (msg.role === 'user') {
                prompt += msg.content + ' ';
            }
        }
        return prompt.trim();
    }
};
