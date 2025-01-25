import React from "react";
import ReactDOM from "react-dom";

function Entry(props) {
  return (
    <div className="description">
      <dl>
        <dt>
          {props.id}
          <span>{props.emoji}</span>
          <span>{props.name}</span>
        </dt>
        <dd>{props.description}</dd>
      </dl>
    </div>
  );
}

export default Entry;
