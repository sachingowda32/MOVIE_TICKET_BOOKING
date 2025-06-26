function showAllReviews() {
    const hiddenReviews = document.querySelectorAll('.review-item.d-none');
    hiddenReviews.forEach(review => {
        review.classList.remove('d-none');
    });

    const button = document.getElementById('show-more-btn');
    if (button) {
        button.style.display = 'none';
    }
}
