const today = new Date();

const day = String(today.getDate()).padStart(2, '0');
const month = String(today.getMonth() + 1).padStart(2, '0'); // Months are zero-based
const year = today.getFullYear();

const formattedDate = `${day}/${month}/${year}`;

console.log("Current Date:", formattedDate);


const today = new Date();
const next30Days = new Date(today);
next30Days.setDate(today.getDate() + 30);

const day = String(next30Days.getDate()).padStart(2, '0');
const month = String(next30Days.getMonth() + 1).padStart(2, '0'); // Months are zero-based
const year = next30Days.getFullYear();

const formattedDate = `${day}/${month}/${year}`;

console.log("Date 30 Days from Now:", formattedDate);
