"""
Amazon Product Scraper
A simple scraper to fetch product data from Amazon search results.
Great for learning Git version control!
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import random

# Headers to mimic a real browser request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}


def scrape_amazon_search(search_query, max_products=10):
    """
    Scrape Amazon search results for a given query.
    
    Args:
        search_query: The product to search for
        max_products: Maximum number of products to return
    
    Returns:
        List of product dictionaries
    """
    # Format the search URL
    search_url = f"https://www.amazon.com/s?k={search_query.replace(' ', '+')}"
    
    products = []
    
    try:
        print(f"Searching Amazon for: {search_query}")
        response = requests.get(search_url, headers=HEADERS, timeout=10)
        
        if response.status_code != 200:
            print(f"Failed to fetch page. Status code: {response.status_code}")
            # Return demo data for practice purposes
            return get_demo_data(search_query, max_products)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find product containers
        product_cards = soup.select('div[data-component-type="s-search-result"]')
        
        if not product_cards:
            print("No products found, using demo data for Git practice")
            return get_demo_data(search_query, max_products)
        
        for card in product_cards[:max_products]:
            product = extract_product_data(card)
            if product:
                products.append(product)
                
        # Small delay to be respectful
        time.sleep(random.uniform(1, 2))
        
    except Exception as e:
        print(f"Error during scraping: {e}")
        print("Using demo data for Git practice")
        return get_demo_data(search_query, max_products)
    
    return products if products else get_demo_data(search_query, max_products)


def extract_product_data(card):
    """
    Extract product information from a search result card.
    
    Args:
        card: BeautifulSoup element containing product info
    
    Returns:
        Dictionary with product data or None
    """
    try:
        # Get ASIN (Amazon's product ID)
        asin = card.get('data-asin', '')
        
        # Get title
        title_elem = card.select_one('h2 a span')
        title = title_elem.get_text(strip=True) if title_elem else 'No title'
        
        # Get price
        price_whole = card.select_one('span.a-price-whole')
        price_fraction = card.select_one('span.a-price-fraction')
        if price_whole:
            price = price_whole.get_text(strip=True).replace(',', '')
            if price_fraction:
                price += price_fraction.get_text(strip=True)
            price = f"${price}"
        else:
            price = 'Price not available'
        
        # Get rating
        rating_elem = card.select_one('span.a-icon-alt')
        rating = rating_elem.get_text(strip=True) if rating_elem else 'No rating'
        
        # Get review count
        review_elem = card.select_one('span.a-size-base.s-underline-text')
        reviews = review_elem.get_text(strip=True) if review_elem else '0'
        
        # Get image URL
        img_elem = card.select_one('img.s-image')
        image_url = img_elem.get('src', '') if img_elem else ''
        
        # Get product URL
        link_elem = card.select_one('h2 a')
        product_url = 'https://www.amazon.com' + link_elem.get('href', '') if link_elem else ''
        
        return {
            'asin': asin,
            'title': title[:100] + '...' if len(title) > 100 else title,
            'price': price,
            'rating': rating,
            'reviews': reviews,
            'image_url': image_url,
            'product_url': product_url
        }
        
    except Exception as e:
        print(f"Error extracting product: {e}")
        return None


def get_demo_data(search_query, count=10):
    """
    Generate demo product data for Git practice.
    This ensures you always have data to work with.
    
    Args:
        search_query: The search term used
        count: Number of demo products to generate
    
    Returns:
        List of demo product dictionaries
    """
    demo_products = [
        {
            'asin': 'B08N5WRWNW',
            'title': 'Premium Dog Food - Grain Free Recipe for Adult Dogs',
            'price': '$54.99',
            'rating': '4.5 out of 5 stars',
            'reviews': '12,847',
            'image_url': 'https://via.placeholder.com/300x300/4A90A4/FFFFFF?text=Dog+Food',
            'product_url': 'https://www.amazon.com/dp/B08N5WRWNW'
        },
        {
            'asin': 'B07D4F5KMN',
            'title': 'Interactive Dog Toy - Puzzle Feeder for Mental Stimulation',
            'price': '$24.99',
            'rating': '4.7 out of 5 stars',
            'reviews': '8,234',
            'image_url': 'https://via.placeholder.com/300x300/FF6B6B/FFFFFF?text=Dog+Toy',
            'product_url': 'https://www.amazon.com/dp/B07D4F5KMN'
        },
        {
            'asin': 'B09XYZ1234',
            'title': 'Orthopedic Dog Bed - Memory Foam for Large Breeds',
            'price': '$89.99',
            'rating': '4.8 out of 5 stars',
            'reviews': '5,621',
            'image_url': 'https://via.placeholder.com/300x300/7CB342/FFFFFF?text=Dog+Bed',
            'product_url': 'https://www.amazon.com/dp/B09XYZ1234'
        },
        {
            'asin': 'B01ABCDEFG',
            'title': 'Cat Tree Tower - Multi-Level with Scratching Posts',
            'price': '$79.99',
            'rating': '4.4 out of 5 stars',
            'reviews': '15,892',
            'image_url': 'https://via.placeholder.com/300x300/9C27B0/FFFFFF?text=Cat+Tree',
            'product_url': 'https://www.amazon.com/dp/B01ABCDEFG'
        },
        {
            'asin': 'B08HIJKLMN',
            'title': 'Automatic Pet Water Fountain - 2L Capacity with Filter',
            'price': '$32.99',
            'rating': '4.6 out of 5 stars',
            'reviews': '9,445',
            'image_url': 'https://via.placeholder.com/300x300/2196F3/FFFFFF?text=Water+Fountain',
            'product_url': 'https://www.amazon.com/dp/B08HIJKLMN'
        },
        {
            'asin': 'B07QRSTUV',
            'title': 'Pet Grooming Kit - Professional Clippers and Scissors Set',
            'price': '$45.99',
            'rating': '4.3 out of 5 stars',
            'reviews': '3,287',
            'image_url': 'https://via.placeholder.com/300x300/FF9800/FFFFFF?text=Grooming+Kit',
            'product_url': 'https://www.amazon.com/dp/B07QRSTUV'
        },
        {
            'asin': 'B06WXYZ789',
            'title': 'Retractable Dog Leash - 26ft Heavy Duty for Large Dogs',
            'price': '$28.99',
            'rating': '4.2 out of 5 stars',
            'reviews': '7,112',
            'image_url': 'https://via.placeholder.com/300x300/795548/FFFFFF?text=Dog+Leash',
            'product_url': 'https://www.amazon.com/dp/B06WXYZ789'
        },
        {
            'asin': 'B09MNOPQRS',
            'title': 'Cat Litter Box - Self-Cleaning Automatic with App Control',
            'price': '$449.99',
            'rating': '4.1 out of 5 stars',
            'reviews': '2,156',
            'image_url': 'https://via.placeholder.com/300x300/607D8B/FFFFFF?text=Litter+Box',
            'product_url': 'https://www.amazon.com/dp/B09MNOPQRS'
        },
        {
            'asin': 'B08TUVWXYZ',
            'title': 'Pet Carrier Backpack - Airline Approved with Ventilation',
            'price': '$59.99',
            'rating': '4.5 out of 5 stars',
            'reviews': '4,789',
            'image_url': 'https://via.placeholder.com/300x300/E91E63/FFFFFF?text=Pet+Carrier',
            'product_url': 'https://www.amazon.com/dp/B08TUVWXYZ'
        },
        {
            'asin': 'B07ABCD123',
            'title': 'Dog Training Treats - Natural Chicken Flavor 1lb Bag',
            'price': '$15.99',
            'rating': '4.7 out of 5 stars',
            'reviews': '18,934',
            'image_url': 'https://via.placeholder.com/300x300/8BC34A/FFFFFF?text=Dog+Treats',
            'product_url': 'https://www.amazon.com/dp/B07ABCD123'
        }
    ]
    
    # Add search context to demo data
    for i, product in enumerate(demo_products[:count]):
        product['search_query'] = search_query
        product['demo_data'] = True
    
    return demo_products[:count]


def save_to_json(products, filename='products.json'):
    """
    Save scraped products to a JSON file.
    
    Args:
        products: List of product dictionaries
        filename: Output filename
    """
    output = {
        'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S'),
        'total_products': len(products),
        'products': products
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(products)} products to {filename}")


def main():
    """Main function to run the scraper."""
    # Default search for pet products (relevant to your marketplace!)
    search_query = "dog toys"
    
    print("=" * 50)
    print("Amazon Product Scraper")
    print("Perfect for Git Practice!")
    print("=" * 50)
    
    # Scrape products
    products = scrape_amazon_search(search_query, max_products=10)
    
    # Save to JSON
    save_to_json(products)
    
    # Print summary
    print("\n" + "=" * 50)
    print(f"Scraped {len(products)} products")
    print("Data saved to products.json")
    print("Open index.html in your browser to view results!")
    print("=" * 50)


if __name__ == '__main__':
    main()