import React, { useState } from "react";

function Items(props) {
  const [isDone, setIsDone] = useState(false);
  function clicked() {
    setIsDone((prevValue) => !prevValue);
  }

  return (
    <li
      onClick={() => props.onChecked(props.id)}

      //   onClick={clicked}
      //   style={{ textDecoration: isDone ? "line-through" : "none" }}
    >
      {props.itemList}
    </li>
  );
}

export default Items;
