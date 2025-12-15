"""
Web Scraper - Using Scraping-Friendly Sites
Perfect for learning Git version control!

This scraper uses sites that explicitly permit scraping:
- books.toscrape.com - Fake bookstore for scraping practice
- quotes.toscrape.com - Quotes database for scraping practice
- scrapethissite.com - Sandbox for web scraping
"""

import requests
from bs4 import BeautifulSoup
import json
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
}


def scrape_books():
    """
    Scrape books from books.toscrape.com
    This site is specifically made for scraping practice!
    
    Returns:
        List of book dictionaries
    """
    url = "https://books.toscrape.com/catalogue/page-2.html"
    books = []
    
    try:
        print(f"Scraping: {url}")
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        if response.status_code != 200:
            print(f"Failed with status: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        book_items = soup.select('article.product_pod')
        
        for item in book_items:
            # Get title
            title_elem = item.select_one('h3 a')
            title = title_elem.get('title', '') if title_elem else 'No title'
            
            # Get price
            price_elem = item.select_one('p.price_color')
            price = price_elem.get_text(strip=True) if price_elem else 'N/A'
            
            # Get rating
            rating_elem = item.select_one('p.star-rating')
            rating_class = rating_elem.get('class', []) if rating_elem else []
            rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
            rating = 0
            for cls in rating_class:
                if cls in rating_map:
                    rating = rating_map[cls]
                    break
            
            # Get image
            img_elem = item.select_one('img')
            image_url = url + img_elem.get('src', '') if img_elem else ''
            
            # Get product link
            link_elem = item.select_one('h3 a')
            product_url = url + 'catalogue/' + link_elem.get('href', '') if link_elem else ''
            
            # Get availability
            avail_elem = item.select_one('p.availability')
            availability = avail_elem.get_text(strip=True) if avail_elem else 'Unknown'
            
            books.append({
                'title': title,
                'price': price,
                'rating': rating,
                'rating_stars': '★' * rating + '☆' * (5 - rating),
                'image_url': image_url,
                'product_url': product_url,
                'availability': availability,
                'source': 'books.toscrape.com'
            })
        
        print(f"Found {len(books)} books")
        
    except Exception as e:
        print(f"Error: {e}")
    
    return books


def scrape_quotes():
    """
    Scrape quotes from quotes.toscrape.com
    Another scraping-friendly practice site!
    
    Returns:
        List of quote dictionaries
    """
    url = "https://quotes.toscrape.com/"
    quotes = []
    
    try:
        print(f"Scraping: {url}")
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        if response.status_code != 200:
            print(f"Failed with status: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        quote_divs = soup.select('div.quote')
        
        for item in quote_divs:
            # Get quote text
            text_elem = item.select_one('span.text')
            text = text_elem.get_text(strip=True) if text_elem else ''
            
            # Get author
            author_elem = item.select_one('small.author')
            author = author_elem.get_text(strip=True) if author_elem else 'Unknown'
            
            # Get tags
            tag_elems = item.select('a.tag')
            tags = [tag.get_text(strip=True) for tag in tag_elems]
            
            quotes.append({
                'text': text,
                'author': author,
                'tags': tags,
                'source': 'quotes.toscrape.com'
            })
        
        print(f"Found {len(quotes)} quotes")
        
    except Exception as e:
        print(f"Error: {e}")
    
    return quotes


def scrape_hockey_teams():
    """
    Scrape hockey team stats from scrapethissite.com
    A sandbox site for web scraping practice!
    
    Returns:
        List of team dictionaries
    """
    url = "https://www.scrapethissite.com/pages/forms/?page_num=15"
    teams = []
    
    try:
        print(f"Scraping: {url}")
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        if response.status_code != 200:
            print(f"Failed with status: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        team_rows = soup.select('tr.team')
        
        for row in team_rows[:15]:  # Limit to 15 teams
            name_elem = row.select_one('td.name')
            name = name_elem.get_text(strip=True) if name_elem else 'Unknown'
            
            year_elem = row.select_one('td.year')
            year = year_elem.get_text(strip=True) if year_elem else 'N/A'
            
            wins_elem = row.select_one('td.wins')
            wins = wins_elem.get_text(strip=True) if wins_elem else '0'
            
            losses_elem = row.select_one('td.losses')
            losses = losses_elem.get_text(strip=True) if losses_elem else '0'
            
            goals_for_elem = row.select_one('td.gf')
            goals_for = goals_for_elem.get_text(strip=True) if goals_for_elem else '0'
            
            goals_against_elem = row.select_one('td.ga')
            goals_against = goals_against_elem.get_text(strip=True) if goals_against_elem else '0'
            
            teams.append({
                'name': name,
                'year': year,
                'wins': int(wins) if wins.isdigit() else 0,
                'losses': int(losses) if losses.isdigit() else 0,
                'goals_for': int(goals_for) if goals_for.isdigit() else 0,
                'goals_against': int(goals_against) if goals_against.isdigit() else 0,
                'source': 'scrapethissite.com'
            })
        
        print(f"Found {len(teams)} teams")
        
    except Exception as e:
        print(f"Error: {e}")
    
    return teams


def save_to_json(data, filename='products.json'):
    """Save scraped data to JSON file."""
    output = {
        'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S'),
        'total_items': len(data.get('books', [])) + len(data.get('quotes', [])) + len(data.get('teams', [])),
        **data
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\nSaved data to {filename}")


def get_demo_books():
    """Demo book data as fallback."""
    return [
        {'title': 'A Light in the Attic', 'price': '£51.77', 'rating': 3, 'rating_stars': '★★★☆☆', 'image_url': 'https://books.toscrape.com/media/cache/fe/72/fe72f0532f7b29c882b4a4c5e3a9b6e5.jpg', 'product_url': '#', 'availability': 'In stock', 'source': 'demo'},
        {'title': 'Tipping the Velvet', 'price': '£53.74', 'rating': 1, 'rating_stars': '★☆☆☆☆', 'image_url': 'https://books.toscrape.com/media/cache/08/e9/08e94f3731d7d6b760dfbfbc02ca5c62.jpg', 'product_url': '#', 'availability': 'In stock', 'source': 'demo'},
        {'title': 'Soumission', 'price': '£50.10', 'rating': 1, 'rating_stars': '★☆☆☆☆', 'image_url': 'https://books.toscrape.com/media/cache/ee/cf/eecf883a3cd4a5a5b tried.jpg', 'product_url': '#', 'availability': 'In stock', 'source': 'demo'},
        {'title': 'Sharp Objects', 'price': '£47.82', 'rating': 4, 'rating_stars': '★★★★☆', 'image_url': 'https://via.placeholder.com/200x250/3498db/fff?text=Sharp+Objects', 'product_url': '#', 'availability': 'In stock', 'source': 'demo'},
        {'title': 'Sapiens: A Brief History', 'price': '£54.23', 'rating': 5, 'rating_stars': '★★★★★', 'image_url': 'https://via.placeholder.com/200x250/9b59b6/fff?text=Sapiens', 'product_url': '#', 'availability': 'In stock', 'source': 'demo'},
        {'title': 'The Requiremnts', 'price': '£22.65', 'rating': 5, 'rating_stars': '★★★★★', 'image_url': 'https://via.placeholder.com/200x250/e74c3c/fff?text=Requirements', 'product_url': '#', 'availability': 'In stock', 'source': 'demo'},
        {'title': 'Mesaerism', 'price': '£33.45', 'rating': 3, 'rating_stars': '★★★☆☆', 'image_url': 'https://via.placeholder.com/200x250/2ecc71/fff?text=Mesmerism', 'product_url': '#', 'availability': 'In stock', 'source': 'demo'},
        {'title': 'Olio', 'price': '£23.88', 'rating': 4, 'rating_stars': '★★★★☆', 'image_url': 'https://via.placeholder.com/200x250/f39c12/fff?text=Olio', 'product_url': '#', 'availability': 'In stock', 'source': 'demo'},
    ]


def get_demo_quotes():
    """Demo quote data as fallback."""
    return [
        {'text': '"The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking."', 'author': 'Albert Einstein', 'tags': ['change', 'deep-thoughts', 'thinking', 'world'], 'source': 'demo'},
        {'text': '"It is our choices, Harry, that show what we truly are, far more than our abilities."', 'author': 'J.K. Rowling', 'tags': ['abilities', 'choices'], 'source': 'demo'},
        {'text': '"There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle."', 'author': 'Albert Einstein', 'tags': ['inspirational', 'life', 'live', 'miracle'], 'source': 'demo'},
        {'text': '"The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid."', 'author': 'Jane Austen', 'tags': ['aliteracy', 'books', 'classic', 'humor'], 'source': 'demo'},
        {'text': '"Imperfection is beauty, madness is genius and it\'s better to be absolutely ridiculous than absolutely boring."', 'author': 'Marilyn Monroe', 'tags': ['be-yourself', 'inspirational'], 'source': 'demo'},
        {'text': '"Try not to become a man of success. Rather become a man of value."', 'author': 'Albert Einstein', 'tags': ['adulthood', 'success', 'value'], 'source': 'demo'},
        {'text': '"It is better to be hated for what you are than to be loved for what you are not."', 'author': 'André Gide', 'tags': ['life', 'love'], 'source': 'demo'},
        {'text': '"I have not failed. I\'ve just found 10,000 ways that won\'t work."', 'author': 'Thomas A. Edison', 'tags': ['edison', 'failure', 'inspirational'], 'source': 'demo'},
    ]


def get_demo_teams():
    """Demo hockey team data as fallback."""
    return [
        {'name': 'Boston Bruins', 'year': '1990', 'wins': 44, 'losses': 24, 'goals_for': 299, 'goals_against': 264, 'source': 'demo'},
        {'name': 'Buffalo Sabres', 'year': '1990', 'wins': 31, 'losses': 30, 'goals_for': 292, 'goals_against': 278, 'source': 'demo'},
        {'name': 'Calgary Flames', 'year': '1990', 'wins': 46, 'losses': 26, 'goals_for': 344, 'goals_against': 263, 'source': 'demo'},
        {'name': 'Chicago Blackhawks', 'year': '1990', 'wins': 49, 'losses': 23, 'goals_for': 284, 'goals_against': 211, 'source': 'demo'},
        {'name': 'Detroit Red Wings', 'year': '1990', 'wins': 34, 'losses': 38, 'goals_for': 273, 'goals_against': 298, 'source': 'demo'},
        {'name': 'Edmonton Oilers', 'year': '1990', 'wins': 37, 'losses': 37, 'goals_for': 272, 'goals_against': 272, 'source': 'demo'},
        {'name': 'Hartford Whalers', 'year': '1990', 'wins': 31, 'losses': 38, 'goals_for': 238, 'goals_against': 276, 'source': 'demo'},
        {'name': 'Los Angeles Kings', 'year': '1990', 'wins': 46, 'losses': 24, 'goals_for': 340, 'goals_against': 254, 'source': 'demo'},
        {'name': 'Minnesota North Stars', 'year': '1990', 'wins': 27, 'losses': 39, 'goals_for': 256, 'goals_against': 266, 'source': 'demo'},
        {'name': 'Montreal Canadiens', 'year': '1990', 'wins': 39, 'losses': 30, 'goals_for': 273, 'goals_against': 249, 'source': 'demo'},
    ]


def main():
    """Main function to run all scrapers."""
    print("=" * 50)
    print("Web Scraper - Scraping-Friendly Sites")
    print("Perfect for Git Practice!")
    print("=" * 50 + "\n")
    
    # Scrape all sources
    books = scrape_books()
    print()
    
    quotes = scrape_quotes()
    print()
    
    teams = scrape_hockey_teams()
    
    # Use demo data if scraping failed
    if not books:
        print("Using demo book data...")
        books = get_demo_books()
    if not quotes:
        print("Using demo quote data...")
        quotes = get_demo_quotes()
    if not teams:
        print("Using demo team data...")
        teams = get_demo_teams()
    
    # Combine all data
    all_data = {
        'books': books,
        'quotes': quotes,
        'teams': teams
    }
    
    # Save to JSON
    save_to_json(all_data)
    
    # Summary
    print("\n" + "=" * 50)
    print("SCRAPING COMPLETE!")
    print(f"  📚 Books: {len(books)}")
    print(f"  💬 Quotes: {len(quotes)}")
    print(f"  🏒 Hockey Teams: {len(teams)}")
    print("=" * 50)
    print("\nOpen index.html in your browser to view results!")


if __name__ == '__main__':
    main()