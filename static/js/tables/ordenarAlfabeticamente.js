export function ordenarColumnaAlfabeticamente(columnId) {

    const columnCells = document.querySelectorAll(`td[data-column="${columnId}"]`);
    const sortedCells = Array.from(columnCells).sort((a, b) => {
        const valueA = getValue(a);
        const valueB = getValue(b);
        return compareValues(valueA, valueB);
    });

    const tbody = document.getElementById("tbodyFaucets");

    sortedCells.forEach(cell => {
        tbody.appendChild(cell.parentElement);
    });
}

function getValue(cell) {
    const textContent = cell.textContent.trim().toLowerCase();
    if (textContent === 'true') {
        return true;
    } else if (textContent === 'false') {
        return false;
    } else {
        return textContent;
    }
}


function compareValues(valueA, valueB) {
    if (typeof valueA === 'boolean' && typeof valueB === 'boolean') {
        return valueA - valueB; // Ordenar booleanos (true primero, luego false)
    }
    return valueA.localeCompare(valueB); // Ordenar texto alfabéticamente
}