"""
Bloomberg Symbol Browser
========================
Browse and search the 3000+ available Bloomberg symbols
"""

import pandas as pd
import sys


def load_symbols():
    """Load symbols from CSV"""
    df = pd.read_csv('BB_symbol.csv')
    # Clean up ticker (remove ' Equity' suffix)
    df['Symbol'] = df['Ticker'].str.replace(' Equity', '', regex=False)
    return df


def show_top_symbols(count=20):
    """Show top symbols by market cap"""
    df = load_symbols()
    print(f"\n{'='*80}")
    print(f"Top {count} Indian Stocks by Market Cap")
    print(f"{'='*80}\n")
    
    for i, row in df.head(count).iterrows():
        symbol = row['Symbol']
        name = row['Short Name']
        mcap = row['Market Cap']
        
        # Format market cap in trillions
        mcap_t = mcap / 1_000_000_000_000
        
        print(f"{i+1:2d}. {symbol:12s} - {name:25s} - ₹{mcap_t:5.1f}T")
    
    print(f"\n{'='*80}\n")


def search_symbols(query):
    """Search for symbols by name or symbol"""
    df = load_symbols()
    query = query.upper()
    
    # Search in symbol or name
    mask = (df['Symbol'].str.contains(query, case=False, na=False) | 
            df['Short Name'].str.contains(query, case=False, na=False))
    
    results = df[mask]
    
    if len(results) == 0:
        print(f"\n❌ No symbols found matching '{query}'\n")
        return
    
    print(f"\n{'='*80}")
    print(f"Search Results for '{query}' ({len(results)} found)")
    print(f"{'='*80}\n")
    
    for i, row in results.head(20).iterrows():
        symbol = row['Symbol']
        name = row['Short Name']
        mcap = row['Market Cap']
        mcap_t = mcap / 1_000_000_000_000
        
        print(f"{symbol:12s} - {name:30s} - ₹{mcap_t:5.2f}T")
    
    if len(results) > 20:
        print(f"\n... and {len(results) - 20} more results")
    
    print(f"\n{'='*80}\n")


def show_sectors():
    """Show symbols grouped by sector (approximate based on name)"""
    df = load_symbols()
    
    sectors = {
        'Banks': ['BANK', 'HDFC', 'ICICI', 'AXIS', 'KOTAK', 'SBI'],
        'IT': ['TECH', 'INFO', 'TCS', 'WIPRO', 'HCL'],
        'Energy': ['OIL', 'COAL', 'NTPC', 'POWER', 'RELIANCE'],
        'Auto': ['MARUTI', 'MAHINDRA', 'TATA MOTORS', 'BAJAJ', 'HERO'],
        'Pharma': ['PHARMA', 'SUN', 'CIPLA', 'REDDY'],
        'Finance': ['FINANCE', 'BAJAJ FIN'],
    }
    
    print(f"\n{'='*80}")
    print(f"Symbols by Sector (Sample)")
    print(f"{'='*80}\n")
    
    for sector, keywords in sectors.items():
        print(f"\n{sector}:")
        print("-" * 40)
        
        mask = df['Short Name'].str.contains('|'.join(keywords), case=False, na=False)
        sector_df = df[mask].head(10)
        
        for _, row in sector_df.iterrows():
            print(f"  {row['Symbol']:12s} - {row['Short Name']}")
    
    print(f"\n{'='*80}\n")


def interactive_mode():
    """Interactive symbol browser"""
    while True:
        print("\n" + "="*80)
        print("Bloomberg Symbol Browser")
        print("="*80)
        print("\nOptions:")
        print("  1. Show top 20 symbols")
        print("  2. Show top 50 symbols")
        print("  3. Search by name or symbol")
        print("  4. Browse by sector")
        print("  5. Export to text file")
        print("  6. Exit")
        print()
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            show_top_symbols(20)
        elif choice == '2':
            show_top_symbols(50)
        elif choice == '3':
            query = input("\nEnter search term: ").strip()
            if query:
                search_symbols(query)
        elif choice == '4':
            show_sectors()
        elif choice == '5':
            export_symbols()
        elif choice == '6':
            print("\nGoodbye!\n")
            break
        else:
            print("\n❌ Invalid choice\n")


def export_symbols():
    """Export all symbols to a text file"""
    df = load_symbols()
    
    filename = "bloomberg_symbols_list.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("Bloomberg Symbols - Complete List\n")
        f.write(f"Total: {len(df)} symbols\n")
        f.write("="*80 + "\n\n")
        
        for i, row in df.iterrows():
            symbol = row['Symbol']
            name = row['Short Name']
            mcap = row['Market Cap']
            mcap_t = mcap / 1_000_000_000_000
            
            f.write(f"{symbol:12s} - {name:30s} - ₹{mcap_t:5.2f}T\n")
    
    print(f"\n✅ Exported {len(df)} symbols to: {filename}\n")


def main():
    if len(sys.argv) > 1:
        # Command line mode
        command = sys.argv[1].lower()
        
        if command == 'top':
            count = int(sys.argv[2]) if len(sys.argv) > 2 else 20
            show_top_symbols(count)
        elif command == 'search':
            if len(sys.argv) < 3:
                print("Usage: python browse_symbols.py search <term>")
            else:
                search_symbols(sys.argv[2])
        elif command == 'sector':
            show_sectors()
        elif command == 'export':
            export_symbols()
        else:
            print("Usage:")
            print("  python browse_symbols.py top [count]")
            print("  python browse_symbols.py search <term>")
            print("  python browse_symbols.py sector")
            print("  python browse_symbols.py export")
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
