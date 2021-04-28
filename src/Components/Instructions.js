import React, { Component } from 'react';

function Instructions() {
    return (
      <div className="instructions">
          <h3>Instructions</h3>
                <ul>
                    <li>Make sure the entire function is enclosed in parentheses</li>
                    <li>Make sure each expression is made up of a a left-expression, operator, right expression enclosed in parentheses.</li>
                </ul>
                <div className="examples">
                <p>Good expression</p><p>Bad expression</p>
                <p>(x*5)</p><p>x*5</p>
                <p>((x+2)+(x^2))</p><p>(x+2+(x^2))</p>
                </div>
      </div>
    );
  }
  export default Instructions;