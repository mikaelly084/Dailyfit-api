document.querySelectorAll(".faq-question").forEach(question => {
  question.addEventListener("click", () => {
    const currentItem = question.parentElement;
    const isActive = currentItem.classList.contains("active");

    document.querySelectorAll(".faq-item").forEach(item => {
      item.classList.remove("active");
    });

    if (!isActive) {
      currentItem.classList.add("active");
    }
  });
});