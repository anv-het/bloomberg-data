"""
Batch Bloomberg Data Downloader
================================
Download Bloomberg data for multiple symbols from BB_symbol.csv

Usage:
    python batch_download.py --count 5
    python batch_download.py --symbols HDFCB,IOCL,RELIANCE
    python batch_download.py --all
"""

import argparse
import pandas as pd
from pathlib import Path
from download_bloomberg_data import BloombergDataDownloader
import time


def load_symbols_from_csv(csv_path: str = "BB_symbol.csv", count: int = None):
    """Load Bloomberg symbols from CSV file"""
    df = pd.read_csv(csv_path)
    
    # Extract symbol from Ticker column (remove " Equity" suffix)
    symbols = df['Ticker'].str.replace(' Equity', '', regex=False).tolist()
    
    if count:
        symbols = symbols[:count]
    
    return symbols


def main():
    parser = argparse.ArgumentParser(
        description='Batch download Bloomberg data for multiple symbols'
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--count', '-c', type=int,
                      help='Download first N symbols from BB_symbol.csv')
    group.add_argument('--symbols', '-s',
                      help='Comma-separated list of symbols (e.g., HDFCB,IOCL,RELIANCE)')
    group.add_argument('--all', '-a', action='store_true',
                      help='Download all symbols from BB_symbol.csv')
    
    parser.add_argument('--output_dir', '-o', default='./output',
                       help='Output directory (default: ./output)')
    parser.add_argument('--template', '-t',
                       default=r'C:\blp\data\FA1_vwijagme.xlsx',
                       help='Bloomberg Excel template path')
    parser.add_argument('--wait', '-w', type=int, default=15,
                       help='Seconds to wait for Bloomberg refresh (default: 15)')
    parser.add_argument('--delay', '-d', type=int, default=5,
                       help='Seconds to wait between downloads (default: 5)')
    
    args = parser.parse_args()
    
    # Get symbols list
    if args.symbols:
        symbols = [s.strip().upper() for s in args.symbols.split(',')]
    elif args.all:
        symbols = load_symbols_from_csv()
    else:
        symbols = load_symbols_from_csv(count=args.count)
    
    print(f"\n{'='*60}")
    print(f"📊 Batch Bloomberg Data Downloader")
    print(f"{'='*60}")
    print(f"Total symbols to download: {len(symbols)}")
    print(f"Output directory: {args.output_dir}")
    print(f"{'='*60}\n")
    
    # Initialize downloader
    try:
        downloader = BloombergDataDownloader(
            template_path=args.template,
            output_dir=args.output_dir
        )
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return
    
    # Download data for each symbol
    results = []
    failed = []
    
    for i, symbol in enumerate(symbols, 1):
        print(f"\n{'='*60}")
        print(f"Progress: [{i}/{len(symbols)}] - {symbol}")
        print(f"{'='*60}\n")
        
        try:
            result = downloader.download_data(symbol, wait_seconds=args.wait)
            if result:
                results.append(result)
            else:
                failed.append(symbol)
        except Exception as e:
            print(f"❌ Failed to download {symbol}: {e}")
            failed.append(symbol)
        
        # Wait before next download (except for last symbol)
        if i < len(symbols):
            print(f"\n⏳ Waiting {args.delay} seconds before next download...")
            time.sleep(args.delay)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"📊 BATCH DOWNLOAD COMPLETE")
    print(f"{'='*60}")
    print(f"✅ Successfully downloaded: {len(results)}")
    print(f"❌ Failed: {len(failed)}")
    
    if results:
        print(f"\n✅ Successful downloads:")
        for r in results:
            print(f"   - {r['symbol']}")
    
    if failed:
        print(f"\n❌ Failed downloads:")
        for s in failed:
            print(f"   - {s}")
    
    print(f"\n📁 All files saved in: {args.output_dir}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
