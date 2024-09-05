#question 1 task 1
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords_review = ["good", "excellent", "bad", "poor", "average"]



def capitalize_keyword(finding_review, keyword_review):
    for keyword in keyword_review:
        finding_review = finding_review.replace(keyword, keyword.upper())
    return finding_review

def process_review(reviews, keyword_review):
    for finding_review in reviews:
        complete_review = capitalize_keyword(finding_review, keyword_review)
        print(complete_review)

process_review(reviews, keywords_review)


#question 1 task 2 
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

equal_all_words = len(positive_words) + len(negative_words)
print(equal_all_words)
