"""
Quick Test Script for Bloomberg Data Downloader
================================================
This script helps you test the Bloomberg downloader with your actual template file.
"""

import os
from pathlib import Path
from download_bloomberg_data import BloombergDataDownloader

def find_template():
    """Find the Bloomberg template file"""
    possible_paths = [
        r"C:\blp\data\FA1_vwijagme.xlsx",
        r"D:\scraping\Bloomberge\FA1_vwijagme.xlsx",
        "./FA1_vwijagme.xlsx",
    ]
    
    for path in possible_paths:
        if Path(path).exists():
            return path
    
    # Search in current directory
    current_dir = Path(".")
    for xlsx in current_dir.glob("*.xlsx"):
        if "FA1" in xlsx.name or "vwijagme" in xlsx.name:
            return str(xlsx)
    
    return None

def main():
    print("\n" + "="*60)
    print("Bloomberg Data Downloader - Quick Test")
    print("="*60 + "\n")
    
    # Find template
    print("🔍 Searching for Bloomberg template file...")
    template = find_template()
    
    if not template:
        print("❌ Template file not found!")
        print("\nPlease specify the path to your Bloomberg Excel template:")
        print("   (e.g., C:\\blp\\data\\FA1_vwijagme.xlsx)")
        template = input("\nTemplate path: ").strip()
        
        if not Path(template).exists():
            print(f"❌ File not found: {template}")
            return
    
    print(f"✅ Template found: {template}\n")
    
    # Get symbol
    print("Available test symbols:")
    print("  - HDFCB (HDFC Bank)")
    print("  - IOCL (Indian Oil Corp)")
    print("  - RELIANCE (Reliance Industries)")
    print("  - TCS (Tata Consultancy)")
    
    symbol = input("\nEnter Bloomberg symbol (without 'IN Equity' suffix): ").strip().upper()
    
    if not symbol:
        symbol = "HDFCB"
        print(f"Using default: {symbol}")
    
    # Warning
    print("\n" + "⚠️ "*20)
    print("IMPORTANT: Make sure Bloomberg Terminal is running!")
    print("⚠️ "*20 + "\n")
    
    proceed = input("Ready to download? (y/n): ").strip().lower()
    
    if proceed != 'y':
        print("Cancelled.")
        return
    
    # Download
    try:
        downloader = BloombergDataDownloader(
            template_path=template,
            output_dir="./output"
        )
        
        result = downloader.download_data(symbol, wait_seconds=20)
        
        if result:
            print("\n" + "="*60)
            print("✅ SUCCESS!")
            print("="*60)
            print(f"\nFiles saved:")
            print(f"  📊 Excel: {result['excel']}")
            print(f"  📄 Values: {result['values']}")
            print(f"  📝 CSV: {result['csv']}")
            print("\n" + "="*60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
