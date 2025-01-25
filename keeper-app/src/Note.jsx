import React from "react";
import DeleteIcon from "@mui/icons-material/Delete";
function Note(props) {
  return (
    <div className="note">
      <h1>{props.title}</h1>
      <p>{props.content}</p>
      <div onClick={props.click}>
        <DeleteIcon />
      </div>
    </div>
  );
}

export default Note;
