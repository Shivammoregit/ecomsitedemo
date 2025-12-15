# Amazon Product Scraper 🛒

A simple Python web scraper that fetches product data from Amazon and displays it in a beautiful HTML interface. **Perfect for learning Git!**

## Project Structure

```
amazon-scraper/
├── scraper.py        # Python scraper script
├── index.html        # HTML display page
├── products.json     # Generated product data
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the scraper:
   ```bash
   python scraper.py
   ```

3. Open `index.html` in your browser to view the results!

## Git Practice Guide 🎓

This project is perfect for learning Git. Here's a step-by-step guide:

### Getting Started

```bash
# Navigate to the project folder
cd amazon-scraper

# Initialize a new Git repository
git init

# Check the status (see all untracked files)
git status

# Add all files to staging
git add .

# Make your first commit
git commit -m "Initial commit: Add scraper and HTML viewer"
```

### Basic Git Commands to Practice

```bash
# View commit history
git log
git log --oneline

# Check current status
git status

# View changes before committing
git diff

# Add specific files
git add scraper.py
git add index.html

# Commit with a message
git commit -m "Your message here"
```

### Branching Practice

```bash
# Create a new branch
git branch feature-new-search

# Switch to the branch
git checkout feature-new-search

# Or create and switch in one command
git checkout -b feature-styling

# List all branches
git branch

# Switch back to main
git checkout main

# Merge a branch
git merge feature-styling

# Delete a branch after merging
git branch -d feature-styling
```

### Suggested Exercises

1. **Exercise 1: Modify the Search Query**
   - Edit `scraper.py` to search for "cat toys" instead of "dog toys"
   - Commit the change with a descriptive message

2. **Exercise 2: Create a Feature Branch**
   - Create a branch called `feature-dark-mode`
   - Modify `index.html` to add a dark/light mode toggle
   - Commit and merge back to main

3. **Exercise 3: Practice Undoing Changes**
   - Make a change you don't want
   - Use `git checkout -- filename` to discard it
   - Or use `git reset HEAD~1` to undo last commit

4. **Exercise 4: View History**
   - Make several commits with different changes
   - Use `git log --oneline --graph` to visualize history

## Files Explained

### scraper.py
- Uses `requests` to fetch Amazon pages
- Uses `BeautifulSoup` to parse HTML
- Extracts product titles, prices, ratings, and images
- Falls back to demo data if scraping fails (Amazon blocks many scraping attempts)

### index.html
- Displays products from `products.json`
- Responsive grid layout
- Amazon-like styling
- Shows demo data if JSON not found

### products.json (generated)
- Created when you run `scraper.py`
- Contains all scraped product data
- Read by `index.html` to display products

## Tips for Git Learning

1. **Commit often** - Make small, focused commits
2. **Write good messages** - Describe what changed and why
3. **Use branches** - Experiment without breaking main code
4. **Check status frequently** - Always know what's staged

## Note on Web Scraping

Amazon actively blocks web scraping. This scraper includes demo data as a fallback so you always have something to work with for Git practice. For production scraping, consider using the official Amazon Product Advertising API or services like Oxylabs.

---

Happy Git learning! 🚀