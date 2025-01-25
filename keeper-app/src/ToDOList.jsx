import React, { useState } from "react";
import Items from "./items";
import InputArea from "./inputArea";
function ToDoList() {
  const [items, setItems] = useState([]);

  function handleAdd(item) {
    setItems((prevItems) => [...prevItems, item]);
  }

  function deleteItem(id) {
    setItems((prevItems) => {
      return prevItems.filter((item, index) => index !== id);
    });
  }
  return (
    <div>
      <div>
        <h3>To-Do List</h3>
      </div>
      <InputArea buttonClicked={handleAdd} />
      <div>
        <ul>
          {items.map((item, index) => (
            <Items
              key={index}
              id={index}
              itemList={item}
              onChecked={deleteItem}
            />
          ))}
        </ul>
      </div>
    </div>
  );
}

export default ToDoList;
