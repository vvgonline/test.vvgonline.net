import json, random

inpath = 'scripts/vikas_qa.jsonl'
outpath = 'scripts/vikas-dataset-augmented.jsonl'

# Load and convert existing entries
converted = []
with open(inpath, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        instr = obj.get('instruction') or obj.get('prompt') or ''
        out = obj.get('output') or obj.get('response') or ''
        converted.append({
            'messages': [
                {'role': 'user', 'content': instr},
                {'role': 'assistant', 'content': out}
            ]
        })

# Generator for 500 new QA pairs (concise, varied, domain-relevant)
topics = [
    'digital transformation', 'change management', 'UX design', 'SEO', 'content marketing',
    'capability building', 'AI in marketing', 'data governance', 'cloud adoption', 'cybersecurity',
    'remote teams', 'vendor selection', 'product strategy', 'design thinking', 'customer journey',
    'lead nurturing', 'personalization', 'headless commerce', 'mobile-first design', 'CDP',
    'A/B testing', 'MVP', 'API strategy', 'MarTech consolidation', 'omnichannel', 'subscription models',
    'serverless', 'digital twin', 'innovation culture', 'digital governance', 'social media intelligence',
    'voice search', 'CDN', 'growth hacking', 'heatmaps', 'composable architecture', 'capability pods',
    'training ROI', 'skills gap', 'performance monitoring', 'observability'
]
metrics = ['conversion rates', 'time-to-value', 'customer lifetime value', 'activation speed', 'retention', 'operational cost', 'time-to-market', 'customer satisfaction']

def make_question(i):
    topic = topics[i % len(topics)]
    metric = metrics[i % len(metrics)]
    return f"How can {topic} improve our {metric}?"


def make_answer(i):
    topic = topics[i % len(topics)]
    metric = metrics[i % len(metrics)]
    tips = {
        'digital transformation': f"Define clear KPIs for {metric}, start with pilot projects, and align leadership to sustain change.",
        'change management': f"Engage stakeholders early, communicate benefits tied to {metric}, and provide targeted training to reduce resistance.",
        'UX design': f"Use user research and prototypes to remove friction that hurts {metric}, then iterate based on analytics.",
        'SEO': f"Optimize content and technical SEO to increase discoverability and organic traffic, improving {metric} over time.",
        'content marketing': f"Produce high-quality, targeted content and measure engagement to steadily lift {metric}.",
        'capability building': f"Train teams on core skills, set quarterly targets, and track {metric} improvements tied to capability growth.",
        'AI in marketing': f"Use predictive models to personalize experiences and automate targeting to boost {metric}.",
        'data governance': f"Create a single source of truth and automated data quality checks so decisions that affect {metric} are reliable.",
        'cloud adoption': f"Migrate incrementally, optimize costs, and use cloud-native services to reduce time-to-market and improve {metric}.",
        'cybersecurity': f"Harden critical systems and implement continuous monitoring so security incidents don't erode {metric}.",
        'remote teams': f"Standardize collaboration tools, clarify outcomes, and measure productivity-related {metric}.",
        'vendor selection': f"Score vendors on strategic fit and expected impact on {metric}; require a proof-of-concept.",
        'product strategy': f"Prioritize features that move the needle on {metric} and use experiments to validate assumptions.",
        'design thinking': f"Run empathy sessions and rapid prototypes focused on concrete outcomes for {metric} to reduce risk.",
        'customer journey': f"Map touchpoints that influence {metric} and optimize the highest-friction steps first.",
        'lead nurturing': f"Segment leads and deliver tailored content to move them through the funnel and improve {metric}.",
        'personalization': f"Start with rules, then introduce ML-based recommendations to increase {metric}.",
        'headless commerce': f"Use headless architecture to deliver faster experiences across channels, helping {metric}.",
        'mobile-first design': f"Prioritize performance and UX on mobile to improve conversions and {metric}.",
        'CDP': f"Unify customer profiles to enable personalized campaigns that lift {metric}.",
        'A/B testing': f"Test changes incrementally and measure impact on {metric} before wide rollout.",
        'MVP': f"Launch a focused MVP to validate assumptions quickly and measure effects on {metric}.",
        'API strategy': f"Expose capabilities via APIs to accelerate integrations that improve {metric}.",
        'MarTech consolidation': f"Rationalize tools to reduce friction and improve data flow that supports {metric}.",
        'omnichannel': f"Deliver consistent experiences across channels to increase loyalty and {metric}.",
        'subscription models': f"Focus on retention-driven product value to grow {metric} over time.",
        'serverless': f"Use serverless for bursty workloads to lower costs and speed delivery affecting {metric}.",
        'digital twin': f"Simulate scenarios to predict impacts on {metric} and reduce implementation risk.",
        'innovation culture': f"Allocate time for experiments and reward learning to surface ideas that improve {metric}.",
        'digital governance': f"Set policies that prioritize high-impact projects and protect {metric} from scope creep.",
        'social media intelligence': f"Monitor sentiment and act on feedback to protect brand and improve {metric}.",
        'voice search': f"Optimize for conversational queries and local intent to capture voice-driven traffic that improves {metric}.",
        'CDN': f"Use a CDN to reduce latency globally and boost performance-related {metric}.",
        'growth hacking': f"Run rapid experiments across channels to find low-cost wins that move {metric}.",
        'heatmaps': f"Use heatmaps to find UX issues and run tests to improve conversion-related {metric}.",
        'composable architecture': f"Build modular systems so teams can iterate faster and impact {metric} quickly.",
        'capability pods': f"Form focused pods with clear KPIs to accelerate improvements in {metric}.",
        'training ROI': f"Tie training outcomes to business metrics so improvements in {metric} are measurable.",
        'skills gap': f"Assess gaps, prioritize high-impact skills, and track {metric} improvements after reskilling.",
        'performance monitoring': f"Instrument key flows to detect regressions and ensure {metric} stays within targets.",
        'observability': f"Combine logs, traces, and metrics so issues impacting {metric} are detected and resolved quickly."
    }
    return tips.get(topic, f"Implement targeted initiatives around {topic} and measure {metric} to iterate quickly.")

# Create 500 new entries
generated = []
for i in range(500):
    q = make_question(i)
    a = make_answer(i)
    generated.append({'messages': [{'role': 'user', 'content': q}, {'role': 'assistant', 'content': a}]})

# Combine converted + generated
all_items = converted + generated

# Write out and validate
with open(outpath, 'w', encoding='utf-8') as f:
    for item in all_items:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

# Validation step: read back and parse each line
with open(outpath, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f, 1):
        json.loads(line)

print(f'Wrote {len(all_items)} JSONL entries to {outpath}')
