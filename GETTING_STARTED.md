# 🚀 Bloomberg Data Downloader - Complete Setup Guide

## ✅ SETUP COMPLETE!

Your Bloomberg data downloader is ready to use! Here's everything you need to know:

---

## 📁 What You Have Now

```
d:\scraping\Bloomberge\
├── ✅ download_bloomberg_data.py   # Main script (single symbol)
├── ✅ batch_download.py             # Batch downloader (multiple symbols)
├── ✅ test_download.py              # Quick test script
├── ✅ setup_and_run.ps1             # Setup automation
├── ✅ requirements.txt               # Python packages
├── ✅ README.md                      # Documentation
├── ✅ BB_symbol.csv                  # 3000+ Indian stock symbols
├── ✅ venv/                         # Virtual environment (READY!)
└── ✅ output/                       # Downloads will go here
```

---

## ⚠️ IMPORTANT: Missing Template File

The script needs the **Bloomberg Excel template with formulas**: `FA1_vwijagme.xlsx`

### Where to get it:
1. **From Bloomberg Terminal**:
   - Go to Bloomberg Terminal
   - Type: `FA` (Financial Analysis)
   - Download/Export the Excel file
   - Save it as: `C:\blp\data\FA1_vwijagme.xlsx`

2. **Or use your existing file**:
   - If you have a Bloomberg FA Excel file
   - Copy it to: `C:\blp\data\FA1_vwijagme.xlsx`
   - Or specify custom path when running script

**Note**: You currently have `FA1_vwijagme_value_copy.xlsx` which is values-only (no formulas). You need the original template with Bloomberg formulas.

---

## 🎯 How to Use

### Option 1: Quick Test (Easiest)

```powershell
# 1. Make sure Bloomberg Terminal is running!

# 2. Activate virtual environment
cd "d:\scraping\Bloomberge"
.\venv\Scripts\Activate.ps1

# 3. Run test script
python test_download.py
```

The test script will:
- ✅ Find your template file automatically
- ✅ Ask which symbol to download
- ✅ Guide you through the process
- ✅ Download and save data

---

### Option 2: Command Line (Full Control)

```powershell
# Activate virtual environment
cd "d:\scraping\Bloomberge"
.\venv\Scripts\Activate.ps1

# Download HDFCB data
python download_bloomberg_data.py --symbol HDFCB

# Download IOCL data
python download_bloomberg_data.py --symbol IOCL

# Download with custom template location
python download_bloomberg_data.py --symbol RELIANCE --template "D:\path\to\template.xlsx"

# Download with longer wait time (if Bloomberg is slow)
python download_bloomberg_data.py --symbol TCS --wait 30
```

---

### Option 3: Batch Download (Multiple Symbols)

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Download first 5 symbols from BB_symbol.csv
python batch_download.py --count 5

# Download specific symbols
python batch_download.py --symbols HDFCB,IOCL,RELIANCE,TCS,BHARTI

# Download first 10 with custom settings
python batch_download.py --count 10 --wait 20 --delay 10
```

---

## 📊 Available Symbols

You have **3000+ Indian stock symbols** in `BB_symbol.csv`:

**Top Companies:**
| Symbol | Company Name | Market Cap |
|--------|-------------|------------|
| RELIANCE | Reliance Industries | ₹20.8 Trillion |
| HDFCB | HDFC Bank Ltd | ₹15.4 Trillion |
| BHARTI | Bharti Airtel | ₹12.6 Trillion |
| TCS | Tata Consultancy | ₹11.7 Trillion |
| ICICIBC | ICICI Bank | ₹10.0 Trillion |
| SBIN | State Bank of India | ₹9.0 Trillion |
| INFO | Infosys Ltd | ₹6.7 Trillion |
| BAF | Bajaj Finance | ₹6.5 Trillion |
| LT | Larsen & Toubro | ₹5.6 Trillion |
| IOCL | Indian Oil Corp | ₹2.3 Trillion |

**Note**: When using the script, **only use the symbol** (e.g., `HDFCB`), not the full ticker (e.g., ~~`HDFCB IN Equity`~~)

---

## 🔧 What the Script Does

### Step-by-Step Process:

1. **Opens your Bloomberg template** (FA1_vwijagme.xlsx)
2. **Replaces the symbol** (e.g., IOCL → HDFCB)
3. **Opens in Excel** to trigger Bloomberg data refresh
4. **Waits 15-30 seconds** for Bloomberg to fetch fresh data
5. **Saves 3 files**:
   - 📊 Excel with formulas (for future refreshes)
   - 📄 Excel values-only (static snapshot)
   - 📝 CSV (for analysis in Python/R)
6. **Closes Excel** and cleans up

---

## 📈 Output Files

For symbol `HDFCB`, you'll get:

```
output/
├── HDFCB_bloomberg_data_20241209_143022.xlsx      # With formulas
├── HDFCB_bloomberg_values_20241209_143022.xlsx    # Values only
└── HDFCB_bloomberg_data_20241209_143022.csv       # CSV export
```

**Data includes:**
- Market Capitalization
- Cash & Equivalents  
- Total Debt
- Enterprise Value
- Revenue (Historical + Estimates)
- EBITDA
- Net Income & EPS
- Cash Flow & CapEx
- Growth rates
- Margins

---

## 🐛 Troubleshooting

### ❌ "Template file not found"

**Solution 1**: Specify template location
```powershell
python download_bloomberg_data.py --symbol HDFCB --template "D:\your\path\FA1_vwijagme.xlsx"
```

**Solution 2**: Copy template to default location
```powershell
# Create directory
mkdir C:\blp\data -Force

# Copy your template there
copy "D:\your\path\FA1_vwijagme.xlsx" "C:\blp\data\FA1_vwijagme.xlsx"
```

---

### ❌ "Bloomberg Terminal must be running"

**Solution**: 
1. Open Bloomberg Terminal
2. Log in completely
3. Wait for it to load
4. Then run the script

---

### ❌ Data not refreshing / Old data

**Solutions**:
1. Increase wait time:
   ```powershell
   python download_bloomberg_data.py --symbol HDFCB --wait 30
   ```

2. Check Bloomberg connection:
   - In Bloomberg Terminal, press `<HELP><HELP>`
   - Check if you're connected

3. Manually refresh once:
   - Open the template in Excel
   - Press `Ctrl+Alt+F9` to refresh all formulas
   - Check if data updates

---

### ❌ Excel closes too early

**Solution**: Increase wait time
```powershell
python download_bloomberg_data.py --symbol HDFCB --wait 25
```

---

### ❌ Import errors after setup

**Solution**: Reinstall packages
```powershell
# Activate venv
.\venv\Scripts\Activate.ps1

# Reinstall
pip install --force-reinstall -r requirements.txt
```

---

## 📝 Examples

### Example 1: Download HDFCB data
```powershell
cd "d:\scraping\Bloomberge"
.\venv\Scripts\Activate.ps1
python download_bloomberg_data.py --symbol HDFCB
```

**Output:**
```
============================================================
📊 Bloomberg Data Downloader
============================================================
Symbol: HDFCB
Output Directory: .\output
============================================================

📝 Replacing IOCL with HDFCB in template...
   ✓ Indian Oil Corp Ltd (IOCL IN) → Indian Oil Corp Ltd (HDFCB IN)
   ✓ Made 5 replacements

🔄 Opening Excel to refresh Bloomberg data...
⏳ Will wait 15 seconds for data refresh...
📊 Creating values-only copy...
💾 Saving files...
✅ Files saved successfully!

============================================================
✅ SUCCESS! Bloomberg data downloaded for HDFCB
============================================================
📁 Output files:
   Excel (with formulas): output\HDFCB_bloomberg_data_20241209.xlsx
   Excel (values only):   output\HDFCB_bloomberg_values_20241209.xlsx
   CSV:                   output\HDFCB_bloomberg_data_20241209.csv
============================================================
```

---

### Example 2: Batch download top 5 banks
```powershell
.\venv\Scripts\Activate.ps1
python batch_download.py --symbols HDFCB,ICICIBC,SBIN,KMB,AXSB
```

---

### Example 3: Download all Nifty 50 stocks
```powershell
# Create a file with Nifty 50 symbols
python batch_download.py --count 50
```

---

## 💡 Pro Tips

1. **Always keep Bloomberg Terminal open** during downloads
2. **First run might be slower** - Bloomberg takes time to connect
3. **Batch downloads**: Use `--delay 10` to give system time between downloads
4. **Large datasets**: Increase `--wait 30` or more
5. **Save templates**: Keep the original Bloomberg template safe
6. **Output organization**: Use `--output_dir` for different projects

---

## 📞 Quick Reference Card

```powershell
# Setup (First time only)
.\setup_and_run.ps1

# Activate environment
.\venv\Scripts\Activate.ps1

# Single download
python download_bloomberg_data.py --symbol <SYMBOL>

# Batch download
python batch_download.py --count <N>

# Test
python test_download.py

# Help
python download_bloomberg_data.py --help
```

---

## ✅ Next Steps

1. **Get the Bloomberg template file** (if you don't have it)
   - Download from Bloomberg Terminal
   - Save as `C:\blp\data\FA1_vwijagme.xlsx`

2. **Test with one symbol**
   ```powershell
   .\venv\Scripts\Activate.ps1
   python test_download.py
   ```

3. **Try batch download**
   ```powershell
   python batch_download.py --count 3
   ```

4. **Automate your workflow**
   - Create batch files for regular updates
   - Schedule with Windows Task Scheduler

---

## 🎉 You're All Set!

Everything is installed and ready. Just:
1. ✅ Get the Bloomberg template
2. ✅ Run Bloomberg Terminal  
3. ✅ Run the script

**Happy data downloading! 📊🚀**

---

*Last updated: December 2024*
*Python 3.11 | Windows | Bloomberg Terminal Required*
