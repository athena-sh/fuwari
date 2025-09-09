#!/usr/bin/env python3

import os
import shutil
import re

def extract_folder_mappings():
    """Extract old->new folder mappings from the redirects file"""
    mappings = {}
    
    with open('public/favicon/_redirects', 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if not line or '/membership' in line or '/subscribe' in line:
            continue
            
        parts = line.split(' ')
        if len(parts) >= 3:
            source = parts[0].strip('/')
            destination = parts[1]
            
            if '/posts/' in destination:
                new_slug = destination.replace('/posts/', '').rstrip('/')
                mappings[source] = new_slug
    
    return mappings

def rename_folders():
    """Rename folder paths to match cleaned slugs"""
    mappings = extract_folder_mappings()
    posts_dir = 'src/content/posts'
    
    if not os.path.exists(posts_dir):
        print(f"Posts directory {posts_dir} not found!")
        return
    
    renamed_count = 0
    skipped_count = 0
    
    # Get current folder names
    existing_folders = [f for f in os.listdir(posts_dir) 
                       if os.path.isdir(os.path.join(posts_dir, f))]
    
    print(f"Found {len(existing_folders)} folders in {posts_dir}")
    print(f"Found {len(mappings)} mappings from redirects")
    
    for old_slug, new_slug in mappings.items():
        old_path = os.path.join(posts_dir, old_slug)
        new_path = os.path.join(posts_dir, new_slug)
        
        # Skip if old folder doesn't exist
        if not os.path.exists(old_path):
            # Check if the new slug already exists (already renamed)
            if os.path.exists(new_path):
                skipped_count += 1
                continue
            else:
                print(f"⚠️  Old folder not found: {old_slug}")
                continue
        
        # Skip if old and new are the same
        if old_slug == new_slug:
            skipped_count += 1
            continue
            
        # Check if destination already exists
        if os.path.exists(new_path):
            print(f"⚠️  Destination already exists: {new_slug} (skipping {old_slug})")
            skipped_count += 1
            continue
        
        try:
            # Rename the folder
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {old_slug} -> {new_slug}")
            renamed_count += 1
        except Exception as e:
            print(f"❌ Error renaming {old_slug} to {new_slug}: {e}")
    
    print(f"\n📊 Summary:")
    print(f"   - Renamed: {renamed_count} folders")
    print(f"   - Skipped: {skipped_count} folders")
    print(f"   - Total processed: {renamed_count + skipped_count}")

if __name__ == '__main__':
    rename_folders()