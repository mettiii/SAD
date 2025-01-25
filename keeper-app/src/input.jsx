import React, { useState } from "react";
import AddIcon from "@mui/icons-material/Add";
import { Fab, Zoom } from "@mui/material";

function Input({ addNote }) {
  const [note, setNote] = useState({ title: "", content: "" });
  const [isExpanded, setIsExpanded] = useState(false);

  function handleChange(event) {
    const { name, value } = event.target;
    setNote((prevValue) => ({ ...prevValue, [name]: value }));
  }

  function handleClick(event) {
    event.preventDefault();
    if (note.title && note.content) {
      addNote(note);
      setNote({ title: "", content: "" });
    }
  }

  function expand() {
    setIsExpanded(true);
  }

  return (
    <div>
      <form>
        {isExpanded && (
          <input
            type="text"
            name="title"
            placeholder="Title"
            value={note.title}
            onChange={handleChange}
          />
        )}
        <br />
        <textarea
          onClick={expand}
          name="content"
          placeholder="Take a note..."
          value={note.content}
          onChange={handleChange}
          row={isExpanded ? 3 : 1}
        ></textarea>
        <br />

        <Zoom in={isExpanded}>
          <Fab onClick={handleClick} onMouseEnter={expand}>
            <AddIcon />
          </Fab>
        </Zoom>
      </form>
    </div>
  );
}

export default Input;
