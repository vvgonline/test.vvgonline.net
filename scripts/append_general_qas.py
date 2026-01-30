import json
from pathlib import Path

outpath = Path('scripts/vikas-dataset-augmented.jsonl')

general_qs = [
    "Hi",
    "Hello",
    "Good morning",
    "Good afternoon",
    "Good evening",
    "How are you?",
    "Can you help me?",
    "Thanks",
    "Thank you",
    "Thanks a lot",
    "I appreciate your help",
    "What's the best way to start a digital transformation?",
    "Can you give a quick tip for improving website conversions?",
    "How do I measure ROI for a pilot project?",
    "What should I ask a vendor in the first meeting?",
    "How can I reduce project delivery risk?",
    "Any advice for managing remote teams effectively?",
    "How do I prioritize capabilities when budget is limited?",
    "What's a simple first experiment for personalization?",
    "How do I get buy-in from leadership?",
    "Is mobile optimization urgent?",
    "How often should we run A/B tests?",
    "What are two quick SEO wins?",
    "How do I track training effectiveness?",
    "What's one metric to watch for customer churn?",
    "How can I use small experiments to reduce risk?",
    "How do I start a content calendar?",
    "Can you summarize a go/no-go checklist for pilots?",
    "What's a good cadence for leadership updates?",
    "How do I define success for a design sprint?",
    "How can we improve site speed quickly?",
    "What should be in a basic data governance checklist?",
    "How can I protect customer data during experiments?",
    "How to onboard a new marketing tool?",
    "Can you suggest a 30-day action plan for digital marketing?",
    "What's a quick way to segment leads?",
    "How do I measure campaign lift?",
    "How to prepare for a vendor proof-of-concept?",
    "What are simple accessibility checks to start with?",
    "How do I write a clear project brief?",
    "What should I include in a one-page digital strategy?",
    "How do I communicate change to staff?",
    "What is a practical first step for vendor consolidation?",
    "How do I welcome feedback from customers?",
    "Can you help me draft a short meeting agenda?",
    "What's a polite follow-up email for a meeting?",
    "How do I politely decline a vendor proposal?"
]

# Templates for professional 2-3 sentence answers
short_answers = {
    'greeting': "Hello — how can I help today? I'm available to provide concise advice or step-by-step actions based on your goals.",
    'thanks': "You're welcome — glad to help. If you'd like, I can expand on any of these points or provide next steps.",
    'how_are_you': "I'm ready to help you with practical guidance. Tell me your priority and I will suggest an actionable plan.",
}

items = []
for q in general_qs[:50]:
    q_text = q
    # craft 2-3 sentence professional actionable answers
    if q.lower() in ['hi','hello','good morning','good afternoon','good evening']:
        a = short_answers['greeting']
    elif 'thank' in q.lower() or 'thanks' in q.lower():
        a = short_answers['thanks']
    elif q.lower() == 'how are you?':
        a = short_answers['how_are_you']
    elif q.lower().startswith('what') and 'digital transformation' in q.lower():
        a = "Start with a small, measurable pilot tied to a clear KPI and executive sponsor. Use the pilot to validate assumptions before scaling." 
    elif 'website conversions' in q.lower():
        a = "Run a conversion audit to identify drop-off points, then prioritize A/B tests on high-traffic pages. Monitor impact for 2-4 weeks before wider rollout." 
    elif 'measure roi' in q.lower() or 'roi' in q.lower():
        a = "Define baseline metrics, estimate incremental benefits and costs, and calculate a simple payback or IRR for the pilot. Re-assess after first measurement period to validate assumptions." 
    elif 'vendor' in q.lower() and 'first meeting' in q.lower():
        a = "Ask about the vendor's proof-of-concept approach, support SLAs, and references from similar customers. Clarify pricing, exit terms, and data ownership up front." 
    elif 'reduce project delivery risk' in q.lower():
        a = "Break work into small milestones with clear acceptance criteria and designated owners. Run regular risk reviews and maintain a mitigation backlog for critical issues." 
    elif 'remote teams' in q.lower():
        a = "Set clear outcome-based goals, standardize collaboration tools, and schedule regular check-ins. Invest in team rituals that maintain culture and psychological safety." 
    elif 'prioritize capabilities' in q.lower():
        a = "Score initiatives by impact and effort, tie them to strategic priorities, and allocate a portion of budget to quick wins. Rebalance quarterly based on results." 
    elif 'personalization' in q.lower():
        a = "Start with rule-based personalization for key segments, instrument outcomes, then iterate to ML-based recommendations. Keep privacy and consent top of mind." 
    elif 'buy-in from leadership' in q.lower():
        a = "Present a concise business case with expected impact and a short pilot plan. Secure an executive sponsor and commit to transparent, regular updates." 
    elif 'mobile optimization' in q.lower():
        a = "Yes — prioritize mobile performance and UX since it affects SEO and conversions. Run an audit and fix high-impact issues like large images and slow third-party scripts." 
    elif 'a/b test' in q.lower():
        a = "Establish clear hypotheses and primary metrics, run tests long enough to reach statistical significance, and use learnings to drive iterative improvements." 
    elif 'seo wins' in q.lower():
        a = "Optimize meta titles and page speed, and fix technical issues like broken links. Prioritize high-intent pages for content improvement." 
    elif 'training effectiveness' in q.lower():
        a = "Measure pre/post assessments, track behavior change on the job, and tie results to business KPIs. Use short refresher sessions to sustain gains." 
    elif 'churn' in q.lower():
        a = "Track engagement decay and recent activity; a leading metric is a sustained drop in core engagement over 30 days. Use targeted retention campaigns for at-risk customers." 
    elif 'small experiments' in q.lower():
        a = "Define a clear hypothesis, run the experiment with controlled scope, and measure a small number of outcome metrics. Scale only once the experiment demonstrates consistent improvement." 
    elif 'content calendar' in q.lower():
        a = "Start with monthly themes aligned to business goals, assign owners, and schedule regular reviews. Use performance data to refine topics and cadence." 
    elif 'go/no-go checklist' in q.lower():
        a = "Include success metrics, resource availability, compliance checks, and a rollback plan. Make the decision against the checklist after the initial pilot period." 
    elif 'leadership updates' in q.lower():
        a = "Use a short weekly or bi-weekly cadence with a one-page status and key risks. Focus leadership time on decisions and removing blockers." 
    elif 'design sprint' in q.lower():
        a = "Define a clear user-centered problem, assemble a small cross-functional team, and set measurable outcomes for the sprint. Test prototypes with target users within the sprint window." 
    elif 'site speed' in q.lower():
        a = "Prioritize image optimization, lazy loading, and reducing unused JavaScript. Measure impact with lab and field metrics to ensure real user improvements." 
    elif 'data governance' in q.lower():
        a = "Define data owners, implement automated quality checks, and document schemas. Start small and expand governance as needs and maturity grow." 
    elif 'protect customer data' in q.lower():
        a = "Apply minimization and anonymization, limit access controls, and ensure consent is captured. Monitor and audit data flows regularly." 
    elif 'onboard a new marketing tool' in q.lower():
        a = "Pilot with a single team, validate API and integration points, and train users before full rollout. Establish tracking to measure the tool's contribution to KPIs." 
    elif '30-day action plan' in q.lower():
        a = "Set 3 concrete goals, run one quick experiment, and ensure measurement is in place. Reassess at 30 days and expand successful tactics." 
    elif 'segment leads' in q.lower():
        a = "Use behavior and firmographic signals to create 3-5 priority segments, then tailor messaging and offers. Track conversion performance per segment and iterate." 
    elif 'campaign lift' in q.lower():
        a = "Use an A/B or holdout group to measure incremental impact versus baseline, and monitor short-term and medium-term effects. Attribute results conservatively." 
    elif 'proof-of-concept' in q.lower():
        a = "Define clear success criteria, minimal scope, and timelines. Ensure data access and test cases are available before starting." 
    elif 'accessibility' in q.lower():
        a = "Start with keyboard navigation, proper alt text, and color contrast checks. Use automated tools and manual testing with assistive tech." 
    elif 'project brief' in q.lower():
        a = "Include objectives, success metrics, scope, timeline, and owner. Keep it one page and focused on outcomes." 
    elif 'one-page digital strategy' in q.lower():
        a = "Summarize vision, top 3 initiatives, target metrics, and required investments. Use it as a living document for leadership alignment." 
    elif 'communicate change' in q.lower():
        a = "Explain the why, the expected benefits, and the concrete steps for affected teams. Provide channels for feedback and support during the transition." 
    elif 'vendor consolidation' in q.lower():
        a = "Start with an audit of existing tools, identify redundancy, and prioritize consolidation based on integration needs and total cost. Run pilots to validate replacements." 
    elif 'welcome feedback' in q.lower():
        a = "Create simple, accessible channels (surveys, in-product prompts) and act on high-frequency themes. Close the loop with customers to show impact." 
    elif 'meeting agenda' in q.lower():
        a = "List the goal, 3 agenda items with timeboxes, and expected decisions. Share the agenda in advance to make meetings efficient." 
    elif 'follow-up email' in q.lower():
        a = "Thank them for their time, summarize key decisions, and list next steps with owners and dates. Keep it short and actionable." 
    elif 'decline a vendor' in q.lower():
        a = "Thank them for the proposal, state the decision briefly, and offer constructive feedback or potential future engagement. Be professional and courteous." 
    else:
        a = "I can help with that — tell me more about your goals and constraints, and I will provide a short, actionable plan."

    items.append({'messages':[{'role':'user','content':q_text},{'role':'assistant','content':a}]})

# Append to file
if outpath.exists():
    with outpath.open('a', encoding='utf-8') as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + '\n')

# Print summary
total = 0
with outpath.open('r', encoding='utf-8') as f:
    for _ in f:
        total += 1
print('Appended', len(items), 'general entries; total lines now', total)
