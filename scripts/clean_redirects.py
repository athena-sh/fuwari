#!/usr/bin/env python3

import re

def clean_slug(slug):
    """Clean up slugs by removing years, stop words, and garbage characters"""
    
    # Remove years (2024, 2025, etc.)
    slug = re.sub(r'-20\d{2}', '', slug)
    
    # Remove common stop words that hurt SEO
    stop_words = [
        '-the-', '-and-', '-or-', '-but-', '-in-', '-on-', '-at-', '-to-', '-for-',
        '-of-', '-with-', '-by-', '-from-', '-up-', '-about-', '-into-', '-through-',
        '-during-', '-before-', '-after-', '-above-', '-below-', '-between-', '-among-',
        '-vs-', '-versus-', '-key-', '-top-', '-best-', '-how-', '-what-', '-why-',
        '-when-', '-where-', '-which-', '-that-', '-this-', '-these-', '-those-'
    ]
    
    for stop_word in stop_words:
        slug = slug.replace(stop_word, '-')
    
    # Remove garbage characters and long alphanumeric strings (like MongoDB IDs)
    slug = re.sub(r'-[a-f0-9]{20,}', '', slug)  # Remove long hex strings
    slug = re.sub(r'-\w{10,}\d+', '', slug)      # Remove long mixed alphanumeric
    
    # Clean up multiple dashes and trailing dashes
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    
    # Specific manual cleanups for better readability
    replacements = {
        'freelance-platforms-direct-clients-differences': 'freelance-platforms-direct-clients',
        'effective-client-communication-strategies-freelancers': 'client-communication-strategies',
        'freelance-contract-essentials': 'freelance-contracts',
        'switch-substack-owning-content-maximize-ad-revenue-today': 'switch-substack-own-content',
        'online-business-legal-essentials': 'online-business-legal-guide',
        'reaching-stars-my-journey-1000-followers-medium-end-day-today': 'reaching-1000-medium-followers',
        'understanding-macronutrients-proteins-carbs-fats': 'macronutrients-guide',
        'effective-workplace-communication-skills-guide': 'workplace-communication-skills',
        '7-proven-strategies-market-freelance-services-social-media': 'market-freelance-services-social-media',
        'mastering-blogging-10-insider-secrets-crafting-irresistible-posts': 'blogging-secrets-irresistible-posts',
        'instagram-marketing-sales-strategies': 'instagram-marketing-strategies',
        'finding-hope-through-writing-my-journey-friends-medium-program': 'finding-hope-writing-medium',
        'ai-generated-story-pandoras-box-fantasy-tale': 'ai-story-pandoras-box',
        'proven-conversion-rate-optimization-techniques': 'conversion-rate-optimization',
        'how-overcome-imposter-syndrome': 'overcome-imposter-syndrome',
        'hydration-myths-water-intake-truths': 'hydration-myths-truths',
        'medium-day-celebrating-better-internet-together': 'medium-day-better-internet',
        'visual-content-creation-tips-non-designers': 'visual-content-non-designers',
        'emotional-intelligence-communication-guide': 'emotional-intelligence-communication',
        'mindfulness-based-cognitive-therapy-guide': 'mindfulness-cognitive-therapy',
        'job-interview-preparation-tips': 'job-interview-tips',
        'mindful-eating-guide-transform-food-relationship': 'mindful-eating-guide',
        'emotional-intelligence-vs-iq-success': 'emotional-intelligence-vs-iq',
        'help-me-surpass-2000-follower-mark-today': 'surpass-2000-followers',
        'mind-bending-journey-history-meditation': 'history-meditation',
        'beating-new-wave-doctors-guide-tackling-new-covid-symptoms-proven-remedies': 'covid-symptoms-remedies',
        'time-management-apps-boost-efficiency': 'time-management-apps',
        'when-change-calls-selling-shoes-tech-economic-principle-shaped-my-life': 'change-calls-economic-principle',
        'video-editing-basics-tools-techniques-beginners': 'video-editing-beginners',
        'dalle-midjourney-ai-art-comparison-pandora': 'dalle-midjourney-ai-art',
        'email-marketing-strategies-entrepreneurs': 'email-marketing-entrepreneurs',
        'create-successful-membership-site-7-steps': 'create-membership-site',
        'monetize-niche-online-community': 'monetize-online-community',
        'monetize-photography-skills-online': 'monetize-photography-skills',
        'time-blocking-vs-do-lists-productivity-comparison': 'time-blocking-vs-todo-lists',
        'rest-recovery-effective-time-management': 'rest-recovery-time-management',
        '7-steps-dominate-mobile-marketing-smartphone-customers': 'mobile-marketing-strategies',
        'reflection-my-journey-back-home': 'journey-back-home',
        'overcoming-imposter-syndrome-career': 'imposter-syndrome-career',
        '7-ways-diversify-freelance-income': 'diversify-freelance-income',
        'finding-career-mentor-benefits': 'career-mentor-benefits',
        'build-high-converting-sales-funnel-digital-products': 'sales-funnel-digital-products',
        'influencer-marketing-strategies-brand-growth': 'influencer-marketing-strategies',
        'winning-corporate-battlefield-unleashing-sun-tzus-secrets-business': 'corporate-sun-tzu-secrets',
        'pajamas-paychecks-freelance-writing-guide': 'freelance-writing-guide',
        'startling-retrospective-journey-tmnt-switch-delivers-arcade-home': 'tmnt-switch-arcade',
        'mindfulness-better-sleep-guide': 'mindfulness-sleep-guide',
        'plant-content-forest-evergreen-strategies-guide': 'evergreen-content-strategies',
        'chatgpt-practical-applications-daily-tasks-guide': 'chatgpt-daily-tasks',
        'seo-fundamentals-content-optimization': 'seo-content-optimization',
        'multitasking-productivity-impact': 'multitasking-productivity',
        '5-meditation-apps-daily-practice': 'meditation-apps-daily-practice',
        'beginners-guide-yoga-flexibility-stress-relief': 'yoga-flexibility-stress-relief',
        'remote-work-success-career-tips': 'remote-work-success',
        'work-life-balance-career-success-strategies': 'work-life-balance-strategies',
        'emotional-intelligence-courses-personal-development': 'emotional-intelligence-courses',
        'best-emotional-intelligence-apps': 'emotional-intelligence-apps',
        'build-successful-online-coaching-empire': 'online-coaching-empire',
        '10-steps-achieve-personal-growth-guide-wayfinder-founder': 'personal-growth-guide',
        'time-management-strategies-career-success': 'time-management-career-success',
        'blog-content-creation-tools-supercharge-your-workflow': 'content-creation-tools',
        '8-step-craft-profitable-online-store': 'craft-profitable-online-store',
        'create-digital-business-plan-beginners-guide': 'digital-business-plan-beginners',
        'mindfulness-lifeline-anxiety-depression': 'mindfulness-anxiety-depression',
        'meditation-cardiovascular-health': 'meditation-heart-health',
        'earn-extra-1200-month-leveraging-affiliate-marketing': 'affiliate-marketing-income',
        'data-analytics-small-online-businesses': 'data-analytics-online-business',
        'build-lasting-healthy-habits': 'lasting-healthy-habits',
        'elon-musk-sells-x-xai': 'elon-musk-x-xai',
        'thinking-fast-slow-unbiased-brief': 'thinking-fast-slow-brief',
        'emotional-intelligence-relationships-guide': 'emotional-intelligence-relationships',
        'magic-user-generated-content-audience-marketers': 'user-generated-content-marketing',
        'sleep-impact-productivity-boost-performance': 'sleep-productivity-performance',
        'essential-content-marketing-strategies-online-business-success': 'content-marketing-online-business',
        'labor-love-crafting-content-calendar-digital-success': 'content-calendar-digital-success',
        'cracking-medium-code-writers-guide-thriving': 'medium-writers-guide',
        'networking-tips-introverts': 'networking-introverts',
        'digital-minimalism-declutter-online-life-boost-focus': 'digital-minimalism-focus',
        'one-thing-turned-around-my-chronic-cold-day': 'chronic-cold-cure',
        'silicon-valleys-shakeup-real-impact-tech-layoffs': 'tech-layoffs-impact',
        'successful-podcast-monetization': 'podcast-monetization',
        'mindfulness-work-tips-strategies': 'mindfulness-work-strategies',
        'good-great-business-excellence-framework': 'business-excellence-framework',
        'theory-practice-leveraging-five-sales-impulses': 'five-sales-impulses',
        'go-viral-tiktok-insider-tips-wannabe-influencer': 'tiktok-viral-tips',
        'use-your-fsa-funds-before-they-expire': 'fsa-funds-expire',
        'sticking-around-30-seconds-medium-pays-off-writers': 'medium-engagement-writers',
        'warm-greeting-jonathan-y-pagoda-lantern-touch-elegance': 'jonathan-y-pagoda-lantern',
        'revenue-revolution-wayfinder-bold-move-medium-skyrocketed-profits-10x': 'wayfinder-revenue-revolution',
        'beginners-guide-different-types-meditation': 'types-meditation-guide',
        'time-tracking-tools-productivity-guide': 'time-tracking-productivity',
        'career-change-industry-switch-guide': 'career-change-guide',
        'travel-blog-monetization-strategies': 'travel-blog-monetization',
        'iphone-pixel-transition-guide': 'iphone-pixel-guide',
        'beginners-guide-mindful-eating': 'mindful-eating-beginners',
        'guard-gold-insiders-guide-fortifying-digital-treasure-chest': 'digital-security-guide',
        'live-streaming-101-captivate-audience-real-time': 'live-streaming-guide',
        'keep-inbox-clutter-free-automate-email-deletion-gmail': 'gmail-automation-clean-inbox',
        'create-sell-productized-services-steps': 'productized-services-guide',
        'surprising-truth-outdoor-exercise-ones-talking': 'outdoor-exercise-benefits',
        '7-mindfulness-techniques-productivity-focus': 'mindfulness-productivity-techniques',
        'storytelling-magic-secret-weapon-irresistible-content': 'storytelling-content-marketing',
        'ten-questions-about-you': 'ten-personal-questions',
        'iterate-your-way-product-market-fit': 'product-market-fit',
        '5-easy-emotional-intelligence-exercises-daily-practice': 'emotional-intelligence-exercises',
        'nutrition-basics-optimal-performance': 'nutrition-optimal-performance',
        'strategic-partnerships-digital-growth': 'strategic-partnerships-growth',
        'time-management-hacks-freelancers': 'freelancer-time-management',
        'create-sell-online-courses': 'create-online-courses',
        'emotional-intelligence-leadership-success-link': 'emotional-intelligence-leadership',
        'online-business-crisis-management-steps': 'business-crisis-management',
        'emotional-intelligence-conflict-resolution-guide': 'emotional-intelligence-conflict',
        'meal-prep-strategies-busy-schedule': 'meal-prep-busy-schedule',
        'identify-career-strengths-weaknesses-growth': 'career-strengths-weaknesses',
        'winning-meddic-elevating-high-value-sales-strategy': 'meddic-sales-strategy',
        'mastering-sales-psychology-5-impulses-drive-consumer-behavior': 'sales-psychology-impulses',
        'googles-700-million-severance-payout-behind-numbers': 'google-severance-payout',
        'emotional-intelligence-stress-management-techniques': 'emotional-intelligence-stress',
        'developing-leadership-skills-team-member-manager': 'leadership-skills-development',
        '7-steps-digital-customer-service-excellence': 'digital-customer-service',
        'digital-business-exit-guide': 'selling-digital-business',
        '10-steps-achieve-personal-growth': 'personal-growth-steps',
        'benefits-morning-routine-mental-physical-health': 'morning-routine-benefits',
        '4-actionable-tips-built-serve-evan-carmichael-catalyze-entrepreneurial-journey': 'entrepreneurial-journey-tips',
        'posture-impact-health': 'posture-health-impact',
        'negotiate-salary-raise-guide': 'salary-negotiation-guide',
        'seo-writing-techniques-content-ranks': 'seo-writing-techniques',
        'content-success-metrics-guide': 'content-metrics-guide',
        'continuing-education-career-relevance': 'continuing-education-career',
        'measuring-emotional-intelligence-assessment-tools': 'emotional-intelligence-assessment',
        'build-thriving-facebook-groups-brand-community': 'facebook-groups-community',
        'emotional-intelligence-mental-health-connection': 'emotional-intelligence-mental-health',
        'mindfulness-vs-meditation-differences': 'mindfulness-vs-meditation',
        'create-sops-business-efficiency': 'sops-business-efficiency',
        '5-game-changing-strategies-boosted-my-workflow': 'workflow-optimization-strategies',
        'become-social-media-manager-guide': 'social-media-manager-guide',
        'last-minute-lifesaver-amazon-gift-cards-holiday-hero': 'amazon-gift-cards-holiday',
        'emotional-intelligence-workplace-importance': 'emotional-intelligence-workplace',
        'create-mindfulness-routine-sticks': 'mindfulness-routine-guide',
        '7-habits-highly-productive-people-boost-efficiency': 'productive-people-habits',
        'monetize-content-different-platforms-insider-tips': 'monetize-content-platforms',
        'linkedin-optimization-tips-boost-online-presence': 'linkedin-optimization-tips',
        'what-is-emotional-intelligence-definition': 'emotional-intelligence-definition',
        'agile-methodologies-digital-entrepreneurship': 'agile-digital-entrepreneurship',
        'eisenhower-matrix-time-management-guide': 'eisenhower-matrix-guide',
        'navigating-office-politics-career-guide': 'office-politics-guide',
        'entrepreneurial-growth-mindset': 'entrepreneurial-mindset',
        'science-meditation-changes-brain': 'meditation-brain-science',
        'mindfulness-meditation-benefits-stress-reduction': 'mindfulness-stress-reduction',
        'mobility-blueprint-kelly-juliet-starrett-get-strong-flexible-built-move': 'mobility-blueprint-starrett',
        'financial-management-steps-digital-entrepreneurs': 'financial-management-entrepreneurs',
        'virtual-assistant-career-guide': 'virtual-assistant-guide',
        'mastering-freelance-pricing-strategies': 'freelance-pricing-strategies',
        'create-freelance-business-website-complete-guide': 'freelance-website-guide',
        'maximize-roi-google-ads-strategies': 'google-ads-roi-strategies',
        'long-term-career-planning-goals-guide': 'career-planning-guide',
        'mindfulness-pain-management-techniques-research': 'mindfulness-pain-management',
        'psychology-procrastination-combat-strategies': 'procrastination-psychology',
        'profitable-food-blog-creation': 'profitable-food-blog',
        'build-engaged-content-community': 'content-community-building',
        'subscription-box-business-guide': 'subscription-box-guide',
        'successful-ghostwriter-guide': 'ghostwriter-guide',
        'components-emotional-intelligence-explained': 'emotional-intelligence-components',
        'become-freelance-writer': 'freelance-writer-guide',
        'creating-your-first-online-course-step-step-guide-beginners': 'create-first-online-course',
        'creating-your-first-online-course-step-step-guide-beginners': 'create-first-online-course',
        '7-tricks-create-irresistible-lead-magnets': 'create-lead-magnets',
        'improve-your-emotional-intelligence-7-practical-steps': 'improve-emotional-intelligence',
        'pinterest-marketing-strategies-boost-traffic-sales': 'pinterest-marketing-strategies',
        'build-affiliate-marketing-passive-income': 'affiliate-marketing-passive-income',
        '2-minute-rule-productivity-hack': 'two-minute-rule-productivity',
        'continuous-learning-freelancing-success': 'continuous-learning-freelancing',
        'online-business-cash-flow-management-strategies': 'cash-flow-management',
        'video-marketing-engagement-strategies': 'video-marketing-strategies',
        'peek-fictional-lives-10-questions-ask-fictional-characters': 'questions-fictional-characters',
        'pomodoro-technique-productivity-boost-25-minute-intervals': 'pomodoro-technique-guide',
        'why-i-became-friend-medium': 'medium-friend-program',
        'science-behind-imposter-syndrome-understanding-psychology': 'imposter-syndrome-psychology',
        '11-essential-freelance-project-management-tips-success': 'freelance-project-management',
        'number-one-secret-elite-use-transform-their-wealth-lifestyle-endless-innovation': 'wealth-transformation-secret',
        'marketing-automation-tools-guide': 'marketing-automation-tools',
        'ultimate-guide-effective-time-blocking': 'time-blocking-guide',
        'hungry-health-my-messy-adventure-intermittent-fasting': 'intermittent-fasting-adventure',
        'mastering-sales-psychology-5-impulses-drive-consumer-behavior-unabridged-version': 'sales-psychology-unabridged',
        'sustainable-online-business-practices': 'sustainable-business-practices',
        'telltale-signs-emotionally-intelligent-leaders': 'emotionally-intelligent-leaders',
        'emotional-intelligence-books-boost-eq': 'emotional-intelligence-books',
        'mastering-freelance-pitch-guide-winning-projects': 'freelance-pitch-guide',
        'enchanting-tale-elfred-shelf': 'elfred-shelf-tale',
        'dark-side-screen-why-dark-mode-is-must-have': 'dark-mode-benefits',
        'importance-soft-skills-career-advancement': 'soft-skills-career',
        'content-repurposing-101-maximize-reach': 'content-repurposing-guide',
        'jalapenos-make-your-day-uncover-their-fiery-benefits': 'jalapenos-health-benefits',
        'master-networking-strategies-freelancers-step-step-guide': 'freelancer-networking-guide',
        'create-sell-digital-products': 'create-digital-products',
        'virtual-tavern-creatives-mediums-innovative-pb-crawl': 'medium-pub-crawl',
        'youtube-monetization-strategies': 'youtube-monetization',
        'labor-day-social-media-strategies-work-smarter': 'labor-day-social-media',
        'cybersecurity-digital-businesses': 'digital-business-security',
        'time-management-strategies-remote-workers': 'remote-worker-time-management',
        'productive-workspace-tips-boost-efficiency': 'productive-workspace-tips',
        'gut-brain-connection-wellness': 'gut-brain-wellness',
        'podcast-production-guide': 'podcast-production',
        'master-social-media-advertising-small-businesses': 'social-media-advertising',
        'zero-booked-land-first-freelance-design-clients': 'first-freelance-design-clients',
        'recovery-techniques-athletes-fitness-enthusiasts': 'athlete-recovery-techniques',
        'yale-emotional-intelligence-course-review-personal-experience': 'yale-emotional-intelligence-course',
        'stress-management-techniques-real-person-guide': 'stress-management-guide',
        'outsourcing-strategies-business-growth': 'outsourcing-business-growth',
        '10-labor-day-social-media-content-ideas': 'labor-day-content-ideas',
        '2000-follower-milestone-achieved-thank-you': 'follower-milestone-thanks',
        'finding-voice-develop-unique-content-brand': 'content-brand-voice',
        'pomodoro-vs-52-17-method-productivity-comparison': 'pomodoro-vs-ultradian-rhythm',
        'scaling-solo-business-hiring-guide': 'scaling-solo-business',
        'time-management-hacks-online-entrepreneurs': 'entrepreneur-time-management',
        'hiit-workout-benefits-lazy-persons-guide': 'hiit-workout-lazy-guide',
        'podcast-marketing-monetization-strategies': 'podcast-marketing-monetization',
        'mindful-movement-meditation-yoga-tai-chi-guide': 'mindful-movement-guide',
        'simple-mindfulness-exercises-beginners': 'mindfulness-exercises-beginners',
        'couch-crush-your-nonsense-guide-strength-training-beginners': 'strength-training-beginners',
        'future-blogging-trends-predictions-beyond': 'blogging-trends-future',
        'creating-personal-brand-career-stand-out': 'personal-brand-career',
        'create-daily-routine-productivity': 'daily-routine-productivity',
        'build-powerful-personal-brand-freelancer-guide': 'freelancer-personal-brand',
        'comparing-emotional-intelligence-certification-programs': 'emotional-intelligence-certification',
        'mindful-parenting-techniques-emotionally-intelligent-kids': 'mindful-parenting-guide',
        'ditch-iphone-verizon-google-pixel-google-fi': 'iphone-google-pixel-switch',
        'gig-economy-successful-freelance-career-guide': 'gig-economy-freelance-guide',
        'developing-emotional-intelligence-children-parents-guide': 'emotional-intelligence-children',
        'side-hustle-ideas-earn-500-3000-month-working-part-time': 'side-hustle-ideas',
        'rise-followayfinder-100-1-google-search': 'wayfinder-seo-success',
        '7-essential-steps-building-personal-brand-online': 'building-personal-brand-online',
        'do-you-feel-invisible-medium': 'feeling-invisible-medium',
        'sleep-personal-growth-connection': 'sleep-personal-growth',
        'smart-goals-benefits-productivity-boost': 'smart-goals-productivity',
        'linkedin-marketing-strategies-b2b-professionals': 'linkedin-b2b-marketing',
        'creating-meditation-space-home-tips': 'meditation-space-home',
        'craft-freelance-portfolio-wow-potential-clients': 'freelance-portfolio-guide',
        'vitamins-supplements-healthy-lifestyle-truth': 'vitamins-supplements-truth',
        'essential-tips-financial-planning-freelancers': 'freelancer-financial-planning',
        'abcde-method-task-prioritization-guide': 'abcde-prioritization-method',
        'ultimate-guide-writing-compelling-resume': 'compelling-resume-guide',
        'start-successful-youtube-channel': 'youtube-channel-guide',
        'scale-freelance-business': 'scaling-freelance-business',
        '7-proven-strategies-handle-difficult-freelance-clients': 'difficult-freelance-clients',
        'must-have-productivity-tools-solopreneurs': 'solopreneur-productivity-tools',
        'power-50-claps-medium-monetization-journey': 'medium-monetization-claps',
        'pricing-digital-products-services': 'digital-product-pricing',
        'beginners-guide-balanced-fitness-plan': 'balanced-fitness-plan',
        'home-gym-heroes-fitness-fortress-budget': 'budget-home-gym-guide',
        'overcome-procrastination-5-proven-strategies-success': 'overcome-procrastination-strategies'
    }
    
    if slug in replacements:
        slug = replacements[slug]
    
    return slug

def process_redirects():
    """Process the redirects file to clean up slugs"""
    with open('public/favicon/_redirects', 'r') as f:
        lines = f.readlines()
    
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Skip external redirects (membership, subscribe)
        if '/membership' in line or '/subscribe' in line:
            cleaned_lines.append(line)
            continue
        
        parts = line.split(' ')
        if len(parts) >= 3:
            source = parts[0]
            destination = parts[1]
            status = parts[2]
            
            # Extract slug from destination (remove /blog/ prefix)
            if '/blog/' in destination:
                slug = destination.replace('/blog/', '').rstrip('/')
                cleaned_slug = clean_slug(slug)
                new_destination = f'/posts/{cleaned_slug}'
                
                # Handle trailing slash version
                if destination.endswith('/'):
                    new_destination += '/'
                
                cleaned_line = f"{source} {new_destination} {status}"
                cleaned_lines.append(cleaned_line)
            else:
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)
    
    # Write cleaned redirects
    with open('public/favicon/_redirects', 'w') as f:
        for line in cleaned_lines:
            f.write(line + '\n')

if __name__ == '__main__':
    process_redirects()
    print("Redirects file cleaned successfully!")