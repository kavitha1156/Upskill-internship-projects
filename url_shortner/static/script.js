function copyLink() {
    const link = document.querySelector(".result a").innerText;
    navigator.clipboard.writeText(link);
    alert("Copied to clipboard!");
}