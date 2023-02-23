import React, { useState } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import predict from './utils/utils';

function CodeEditor() {
  const [value, setValue] = useState('');

  const onChangeText = (e) => {
    const predictedWord = predict(e);
    setValue(predictedWord);
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
