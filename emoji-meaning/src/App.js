import Entry from "../src/component/Entry";
import React from "react";
import emojiDictionary from "./Emojies";

function displayEmoji(emojiTerm) {
  return (
    <Entry
      id={emojiTerm.id}
      key={emojiTerm.id}
      emoji={emojiTerm.emoji}
      name={emojiTerm.name}
      description={emojiTerm.description}
    />
  );
}

function App() {
  return (
    <div>
      <h1>Emoji DIctionary</h1>
      {emojiDictionary.map((emojiTerm) => (
        <Entry
          id={emojiTerm.id}
          key={emojiTerm.id}
          emoji={emojiTerm.emoji}
          name={emojiTerm.name}
          description={emojiTerm.description}
        />
      ))}
      ;
    </div>
  );
}

export default App;
