import React, { useState } from "react";
import "./App.css";
import Header from "./Header";
import Footer from "./Footer";
import Note from "./Note";
import ToDoList from "./ToDOList";
import Input from "./input";
function App() {
  const [notes, setNotes] = useState([]);

  function deleteNote(id) {
    setNotes((prevNotes) => prevNotes.filter((_, index) => index !== id));
  }

  const addNote = (note) => {
    setNotes((prevNotes) => [...prevNotes, note]);
  };

  const createNote = (noteItem, index) => {
    return (
      <Note
        key={index}
        title={noteItem.title}
        content={noteItem.content}
        click={() => deleteNote(index)}
      />
    );
  };

  return (
    <div>
      <Header />
      <Input addNote={addNote} />
      <div id="list">{notes.map(createNote)}</div>
      <ToDoList />
      <Footer />
    </div>
  );
}

export default App;
