import React, { useState } from "react";

function InputArea(props) {
  const [item, setItem] = useState("");
  function handleChange(event) {
    setItem(event.target.value);
  }

  return (
    <div>
      <input type="text" name="items" value={item} onChange={handleChange} />
      <input
        type="button"
        value="Add"
        onClick={() => {
          props.buttonClicked(item);
          setItem("");
        }}
      />
    </div>
  );
}
export default InputArea;
