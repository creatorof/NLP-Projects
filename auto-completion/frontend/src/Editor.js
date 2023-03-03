import React, { useState } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';

function CodeEditor() {
  const [value, setValue] = useState('');

  const onChangeText = (e) => {
    const sentence = {
      sentence: e.target.value,
    };
    axios
      .post('http://127.0.0.1:5000/autocomplete', sentence, {
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then((res) => {
        const predictedWord = res.data.predicted;
        const sentence = value + predictedWord;
        setValue(sentence);
      })
      .catch((err) => {
        console.log(err);
      });
  };
  return (
    <ReactQuill
      className="text-editor-container"
      theme="snow"
      value={value}
      onChange={onChangeText}
    />
  );
}

export default CodeEditor;
