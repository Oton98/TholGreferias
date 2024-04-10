export function getIdFromURL() {
    const urlParts = window.location.pathname.split('/');
    const productId = urlParts[urlParts.length - 1];
    return productId;
}