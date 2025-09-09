#!/usr/bin/env python3

import os
import re

def get_ultra_concise_mappings():
    """Ultra-concise slug mappings - much shorter and punchier"""
    return {
        # Communication & Freelancing
        'effective-client-communication-strategies-freelancers': 'client-communication',
        'freelance-platforms-direct-clients-differences': 'freelance-platforms',
        'freelance-contract-essentials': 'freelance-contracts',
        'freelance-writing-guide': 'freelance-writing',
        'freelancer-time-management': 'freelance-time',
        'freelance-pricing-strategies': 'freelance-pricing',
        'freelance-website-guide': 'freelance-website',
        'freelance-project-management': 'freelance-projects',
        'freelance-pitch-guide': 'freelance-pitch',
        'freelancer-networking-guide': 'freelance-network',
        'freelancer-personal-brand': 'freelance-brand',
        'freelancer-financial-planning': 'freelance-finance',
        'difficult-freelance-clients': 'difficult-clients',
        'scaling-freelance-business': 'scale-freelance',
        'first-freelance-design-clients': 'first-clients',
        'diversify-freelance-income': 'freelance-income',
        'continuous-learning-freelancing': 'freelance-learning',
        'gig-economy-freelance-guide': 'gig-economy',
        
        # Business & Entrepreneurship
        'online-business-legal-guide': 'business-legal',
        'digital-business-plan-beginners': 'business-plan',
        'selling-digital-business': 'sell-business',
        'business-crisis-management': 'crisis-management',
        'business-excellence-framework': 'business-excellence',
        'sustainable-business-practices': 'sustainable-business',
        'digital-business-security': 'business-security',
        'outsourcing-business-growth': 'outsourcing',
        'agile-digital-entrepreneurship': 'agile-business',
        'entrepreneurial-mindset': 'entrepreneur-mindset',
        'entrepreneurial-journey-tips': 'entrepreneur-tips',
        'strategic-partnerships-growth': 'partnerships',
        'cash-flow-management': 'cash-flow',
        'financial-management-entrepreneurs': 'business-finance',
        'sops-business-efficiency': 'sops',
        
        # Marketing & Sales
        'market-freelance-services-social-media': 'market-services',
        'instagram-marketing-strategies': 'instagram-marketing',
        'email-marketing-entrepreneurs': 'email-marketing',
        'sales-funnel-digital-products': 'sales-funnel',
        'influencer-marketing-strategies': 'influencer-marketing',
        'conversion-rate-optimization': 'conversion-optimization',
        'content-marketing-online-business': 'content-marketing',
        'user-generated-content-marketing': 'ugc-marketing',
        'storytelling-content-marketing': 'storytelling',
        'video-marketing-strategies': 'video-marketing',
        'mobile-marketing-strategies': 'mobile-marketing',
        'pinterest-marketing-strategies': 'pinterest-marketing',
        'linkedin-b2b-marketing': 'linkedin-marketing',
        'social-media-advertising': 'social-ads',
        'google-ads-roi-strategies': 'google-ads',
        'marketing-automation-tools': 'marketing-automation',
        'facebook-groups-community': 'facebook-groups',
        'labor-day-social-media': 'labor-day-content',
        'labor-day-content-ideas': 'labor-day-ideas',
        'tiktok-viral-tips': 'tiktok-viral',
        'podcast-marketing-monetization': 'podcast-marketing',
        'youtube-monetization': 'youtube-money',
        'linkedin-optimization-tips': 'linkedin-tips',
        
        # Content Creation
        'blogging-secrets-irresistible-posts': 'blogging-secrets',
        'content-creation-tools': 'content-tools',
        'content-calendar-digital-success': 'content-calendar',
        'content-metrics-guide': 'content-metrics',
        'content-repurposing-guide': 'content-repurposing',
        'content-brand-voice': 'brand-voice',
        'content-community-building': 'content-community',
        'evergreen-content-strategies': 'evergreen-content',
        'seo-content-optimization': 'seo-content',
        'seo-writing-techniques': 'seo-writing',
        'visual-content-non-designers': 'visual-content',
        'create-online-courses': 'online-courses',
        'create-first-online-course': 'first-course',
        'create-lead-magnets': 'lead-magnets',
        'create-membership-site': 'membership-site',
        'create-digital-products': 'digital-products',
        'productized-services-guide': 'productized-services',
        'subscription-box-guide': 'subscription-box',
        'ghostwriter-guide': 'ghostwriting',
        'monetize-content-platforms': 'monetize-content',
        'monetize-online-community': 'monetize-community',
        'monetize-photography-skills': 'monetize-photos',
        'affiliate-marketing-income': 'affiliate-income',
        'affiliate-marketing-passive-income': 'passive-income',
        'profitable-food-blog': 'food-blog',
        'travel-blog-monetization': 'travel-blog',
        'podcast-monetization': 'podcast-money',
        'digital-product-pricing': 'product-pricing',
        
        # Productivity & Time Management
        'time-management-career-success': 'time-management',
        'remote-worker-time-management': 'remote-time',
        'entrepreneur-time-management': 'entrepreneur-time',
        'time-blocking-guide': 'time-blocking',
        'time-blocking-do-lists-productivity-comparison': 'time-blocking-vs-todos',
        'time-tracking-productivity': 'time-tracking',
        'rest-recovery-time-management': 'rest-recovery',
        'eisenhower-matrix-guide': 'eisenhower-matrix',
        'abcde-prioritization-method': 'abcde-method',
        'two-minute-rule-productivity': 'two-minute-rule',
        'pomodoro-technique-guide': 'pomodoro-technique',
        'pomodoro-52-17-method-productivity-comparison': 'pomodoro-vs-ultradian',
        'multitasking-productivity': 'multitasking',
        'productive-people-habits': 'productivity-habits',
        'productive-workspace-tips': 'workspace-tips',
        'workflow-optimization-strategies': 'workflow-optimization',
        'solopreneur-productivity-tools': 'productivity-tools',
        'smart-goals-productivity': 'smart-goals',
        'overcome-procrastination-strategies': 'beat-procrastination',
        'procrastination-psychology': 'procrastination',
        'daily-routine-productivity': 'daily-routine',
        'scaling-solo-business': 'scale-solo',
        
        # Health & Wellness
        'macronutrients-guide': 'macronutrients',
        'hydration-myths-truths': 'hydration-myths',
        'nutrition-optimal-performance': 'nutrition',
        'meal-prep-busy-schedule': 'meal-prep',
        'mindful-eating-guide': 'mindful-eating',
        'mindful-eating-beginners': 'mindful-eating-basics',
        'lasting-healthy-habits': 'healthy-habits',
        'intermittent-fasting-adventure': 'intermittent-fasting',
        'vitamins-supplements-truth': 'supplements',
        'jalapenos-health-benefits': 'jalapenos',
        'gut-brain-wellness': 'gut-brain',
        'posture-health-impact': 'posture',
        'outdoor-exercise-benefits': 'outdoor-exercise',
        'surprising-truth-outdoor-exercise-ones-talking-about': 'outdoor-exercise-truth',
        'balanced-fitness-plan': 'fitness-plan',
        'budget-home-gym-guide': 'home-gym',
        'strength-training-beginners': 'strength-training',
        'hiit-workout-lazy-guide': 'hiit-workout',
        'athlete-recovery-techniques': 'recovery',
        'yoga-flexibility-stress-relief': 'yoga',
        'mobility-blueprint-starrett': 'mobility',
        
        # Mental Health & Personal Development
        'overcome-imposter-syndrome': 'imposter-syndrome',
        'imposter-syndrome-career': 'career-imposter',
        'imposter-syndrome-psychology': 'imposter-psychology',
        'emotional-intelligence-communication': 'eq-communication',
        'emotional-intelligence-relationships': 'eq-relationships',
        'emotional-intelligence-leadership': 'eq-leadership',
        'emotional-intelligence-workplace': 'eq-workplace',
        'emotional-intelligence-mental-health': 'eq-mental-health',
        'emotional-intelligence-stress': 'eq-stress',
        'emotional-intelligence-conflict': 'eq-conflict',
        'emotional-intelligence-exercises': 'eq-exercises',
        'emotional-intelligence-assessment': 'eq-assessment',
        'emotional-intelligence-apps': 'eq-apps',
        'emotional-intelligence-courses': 'eq-courses',
        'emotional-intelligence-books': 'eq-books',
        'emotional-intelligence-definition': 'eq-definition',
        'emotional-intelligence-components': 'eq-components',
        'emotional-intelligence-certification': 'eq-certification',
        'emotional-intelligence-children': 'eq-kids',
        'emotionally-intelligent-leaders': 'eq-leaders',
        'yale-emotional-intelligence-course': 'yale-eq-course',
        'improve-emotional-intelligence': 'improve-eq',
        'personal-growth-steps': 'personal-growth',
        'personal-brand-career': 'personal-brand',
        'building-personal-brand-online': 'online-brand',
        'sleep-personal-growth': 'sleep-growth',
        'mindfulness-anxiety-depression': 'mindfulness-anxiety',
        'mindfulness-stress-reduction': 'mindfulness-stress',
        'mindfulness-work-strategies': 'mindfulness-work',
        'mindfulness-routine-guide': 'mindfulness-routine',
        'mindfulness-exercises-beginners': 'mindfulness-basics',
        'mindfulness-productivity-techniques': 'mindfulness-productivity',
        'mindfulness-cognitive-therapy': 'mindfulness-therapy',
        'mindfulness-sleep-guide': 'mindfulness-sleep',
        'mindfulness-pain-management': 'mindfulness-pain',
        'mindfulness-meditation-differences': 'mindfulness-vs-meditation',
        'mindful-movement-guide': 'mindful-movement',
        'mindful-parenting-guide': 'mindful-parenting',
        'stress-management-guide': 'stress-management',
        
        # Career & Professional Development
        'workplace-communication-skills': 'workplace-communication',
        'remote-work-success': 'remote-work',
        'work-life-balance-strategies': 'work-life-balance',
        'career-mentor-benefits': 'career-mentor',
        'career-change-guide': 'career-change',
        'career-planning-guide': 'career-planning',
        'career-strengths-weaknesses': 'career-strengths',
        'continuing-education-career': 'continuing-education',
        'job-interview-tips': 'interview-tips',
        'salary-negotiation-guide': 'salary-negotiation',
        'compelling-resume-guide': 'resume-guide',
        'office-politics-guide': 'office-politics',
        'leadership-skills-development': 'leadership-skills',
        'soft-skills-career': 'soft-skills',
        'networking-introverts': 'networking',
        'virtual-assistant-guide': 'virtual-assistant',
        'social-media-manager-guide': 'social-media-manager',
        'digital-customer-service': 'customer-service',
        
        # Meditation & Mindfulness
        'meditation-apps-daily-practice': 'meditation-apps',
        'types-meditation-guide': 'meditation-types',
        'history-meditation': 'meditation-history',
        'meditation-brain-science': 'meditation-science',
        'meditation-heart-health': 'meditation-health',
        'meditation-space-home': 'meditation-space',
        'morning-routine-benefits': 'morning-routine',
        'sleep-productivity-performance': 'sleep-productivity',
        
        # Technology & Digital
        'chatgpt-daily-tasks': 'chatgpt-tasks',
        'ai-story-pandoras-box': 'ai-story',
        'dalle-midjourney-ai-art': 'ai-art',
        'video-editing-beginners': 'video-editing',
        'live-streaming-guide': 'live-streaming',
        'podcast-production': 'podcast-production',
        'youtube-channel-guide': 'youtube-guide',
        'iphone-pixel-guide': 'iphone-pixel',
        'iphone-google-pixel-switch': 'pixel-switch',
        'gmail-automation-clean-inbox': 'gmail-automation',
        'digital-minimalism-focus': 'digital-minimalism',
        'digital-security-guide': 'digital-security',
        'dark-mode-benefits': 'dark-mode',
        'dark-side-screen-dark-mode-is-must-have': 'dark-mode-guide',
        
        # Business Stories & Case Studies
        'reaching-1000-medium-followers': 'medium-1000',
        'finding-hope-writing-my-journey-friends-medium-program': 'medium-journey',
        'medium-day-better-internet': 'medium-day',
        'medium-writers-guide': 'medium-guide',
        'medium-friend-program': 'medium-friend',
        'medium-monetization-claps': 'medium-claps',
        'medium-engagement-writers': 'medium-engagement',
        'feeling-invisible-medium': 'medium-invisible',
        'medium-pub-crawl': 'medium-crawl',
        'wayfinder-revenue-revolution': 'wayfinder-revenue',
        'wayfinder-seo-success': 'wayfinder-seo',
        'change-calls-economic-principle': 'economic-principle',
        'covid-symptoms-remedies': 'covid-remedies',
        'tech-layoffs-impact': 'tech-layoffs',
        'google-severance-payout': 'google-severance',
        'elon-musk-x-xai': 'musk-x-xai',
        'thinking-fast-slow-brief': 'thinking-fast-slow',
        'corporate-sun-tzu-secrets': 'sun-tzu-business',
        'tmnt-switch-arcade': 'tmnt-arcade',
        'jonathan-y-pagoda-lantern': 'pagoda-lantern',
        'elfred-shelf-tale': 'elfred-tale',
        'amazon-gift-cards-holiday': 'amazon-gifts',
        'follower-milestone-thanks': 'milestone-thanks',
        'data-analytics-online-business': 'business-analytics',
        
        # Sales & Psychology
        'sales-psychology-impulses': 'sales-psychology',
        'sales-psychology-unabridged': 'sales-psychology-full',
        'five-sales-impulses': 'sales-impulses',
        'meddic-sales-strategy': 'meddic-sales',
        'wealth-transformation-secret': 'wealth-secret',
        'product-market-fit': 'product-fit',
        
        # Misc & Lifestyle
        'ten-questions-you': 'ten-questions',
        'questions-fictional-characters': 'fictional-questions',
        'side-hustle-ideas': 'side-hustles',
        'best-side-hustle-ideas-earn-500-3000-month-working-part-time': 'side-hustle-500-3000',
        'use-your-fsa-funds-they-expire': 'fsa-funds',
        'craft-profitable-online-store': 'online-store',
        'online-coaching-empire': 'coaching-business',
        'blogging-trends-future': 'blogging-trends',
        '10-steps-achieve-self-personal-growth-guide-wayfinder-founder': 'self-growth-guide',
        'this-one-thing-turned-around-my-chronic-cold-day': 'chronic-cold-cure',
        'this-is-you-become-freelance-writer': 'become-writer',
        'how-start-successful-youtube-channel': 'start-youtube',
        'hungry-health-my-messy-adventure-intermittent-fasting': 'fasting-adventure',
        'best-marketing-automation-tools-guide': 'automation-tools',
        'top-emotional-intelligence-courses-personal-development': 'top-eq-courses',
        'best-emotional-intelligence-books-boost-eq': 'best-eq-books',
        'help-me-surpass-follower-mark-today': 'surpass-followers'
    }

def update_redirects_with_ultra_concise():
    """Update redirects file with ultra-concise slugs"""
    mappings = get_ultra_concise_mappings()
    
    # Read current redirects
    with open('public/favicon/_redirects', 'r') as f:
        lines = f.readlines()
    
    updated_lines = []
    update_count = 0
    
    for line in lines:
        line = line.strip()
        if not line or '/membership' in line or '/subscribe' in line:
            updated_lines.append(line)
            continue
        
        parts = line.split(' ')
        if len(parts) >= 3:
            source = parts[0]
            destination = parts[1]
            status = parts[2]
            
            # Extract current slug from destination
            if '/posts/' in destination:
                current_slug = destination.replace('/posts/', '').rstrip('/')
                
                # Check if we have a mapping for this slug
                if current_slug in mappings:
                    new_slug = mappings[current_slug]
                    new_destination = f'/posts/{new_slug}'
                    
                    # Handle trailing slash
                    if destination.endswith('/'):
                        new_destination += '/'
                    
                    updated_line = f"{source} {new_destination} {status}"
                    updated_lines.append(updated_line)
                    update_count += 1
                    print(f"✅ Updated: {current_slug} -> {new_slug}")
                else:
                    updated_lines.append(line)
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    
    # Write updated redirects
    with open('public/favicon/_redirects', 'w') as f:
        for line in updated_lines:
            f.write(line + '\n')
    
    print(f"\n📊 Updated {update_count} redirects with ultra-concise slugs!")
    return mappings

def rename_folders_to_ultra_concise():
    """Rename folders to match ultra-concise slugs"""
    mappings = get_ultra_concise_mappings()
    posts_dir = 'src/content/posts'
    
    renamed_count = 0
    
    for old_slug, new_slug in mappings.items():
        old_path = os.path.join(posts_dir, old_slug)
        new_path = os.path.join(posts_dir, new_slug)
        
        # Skip if old folder doesn't exist
        if not os.path.exists(old_path):
            continue
        
        # Skip if already renamed
        if old_slug == new_slug:
            continue
            
        # Check if destination already exists
        if os.path.exists(new_path):
            print(f"⚠️  Destination exists: {new_slug} (skipping {old_slug})")
            continue
        
        try:
            # Rename the folder
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {old_slug} -> {new_slug}")
            renamed_count += 1
        except Exception as e:
            print(f"❌ Error renaming {old_slug} to {new_slug}: {e}")
    
    print(f"\n📊 Renamed {renamed_count} folders to ultra-concise slugs!")

if __name__ == '__main__':
    print("🚀 Starting ultra-concise slug optimization...")
    print("\n1. Updating redirects file...")
    mappings = update_redirects_with_ultra_concise()
    
    print("\n2. Renaming folders...")
    rename_folders_to_ultra_concise()
    
    print(f"\n🎉 Ultra-concise optimization complete!")
    print(f"   - Total mappings: {len(mappings)}")
    print(f"   - Slugs are now much shorter and punchier!")
    
    print(f"\n🔥 Examples of improvements:")
    examples = [
        ('effective-client-communication-strategies-freelancers', 'client-communication'),
        ('emotional-intelligence-leadership-success-link', 'eq-leadership'),
        ('7-mindfulness-techniques-productivity-focus', 'mindfulness-productivity'),
        ('dark-side-screen-why-dark-mode-is-must-have', 'dark-mode'),
        ('sales-psychology-5-key-impulses-drive-consumer-behavior', 'sales-psychology'),
        ('overcome-procrastination-5-proven-strategies-success', 'beat-procrastination')
    ]
    
    for old, new in examples:
        if old in mappings:
            print(f"   - {old} -> {new}")