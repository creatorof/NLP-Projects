import React, { useState } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';

function CodeEditor() {
  const [value, setValue] = useState('');

  const onChangeText = (e) => {
    setValue(e);
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
