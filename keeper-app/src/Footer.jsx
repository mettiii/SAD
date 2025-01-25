import React from "react";

const currentDate = new Date();
const year = currentDate.getFullYear();
const name = "Meti Abera";

function Footer() {
  return (
    <footer>
      <p>Created by {name}</p>
      <p>Copyright © {year}</p>
    </footer>
  );
}

export default Footer;
