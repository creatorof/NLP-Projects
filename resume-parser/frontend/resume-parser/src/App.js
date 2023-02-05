import './App.css';
import React from 'react';
import { useState } from 'react';

function App() {
  // drag state
  const [dragActive, setDragActive] = React.useState(false);
  // ref
  const inputRef = React.useRef(null);
  const [formData, setFormData] = useState([]);
  // handle drag events
  const handleDrag = function (e) {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  // triggers when file is dropped
  const handleDrop = function (e) {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length >= 1) {
      console.log(e.dataTransfer.files);
      // handleFiles(e.dataTransfer.files);
      setFormData((formData) => [...formData, ...e.dataTransfer.files]);
    }
  };

  // triggers when file is selected with click
  const handleChange = function (e) {
    e.preventDefault();
    console.log(e.target.files);
    debugger;
    if (e.target.files && e.target.files.length >= 1) {
      setFormData((formData) => [...formData, ...e.target.files]);
    }
  };

  // triggers the input when the button is clicked
  const onButtonClick = () => {
    inputRef.current.click();
  };

  const onSubmit = (e) => {
    debugger;
    e.preventDefault();
    console.log(formData);
    // const formData = new FormData();
    // formData.append('file', e.target.file[0]);
    // const res = await fetch('http://localhost:5000/upload-file', {
    //   method: 'POST',
    //   body: formData,
    // }).then((res) => res.json());
    // alert(JSON.stringify(`${res.message}, status: ${res.status}`));
  };

  return (
    <div className="page">
      <form id="form-file-upload" onDragEnter={handleDrag} onSubmit={onSubmit}>
        <input
          ref={inputRef}
          type="file"
          id="input-file-upload"
          accept=".pdf,.doc,.docx"
          multiple={true}
          onChange={handleChange}
        />
        <label
          id="label-file-upload"
          htmlFor="input-file-upload"
          className={dragActive ? 'drag-active' : ''}
        >
          <div>
            <p>Drag and drop your resume here or</p>
            <button className="upload-button" onClick={onButtonClick}>
              Upload a Resume
            </button>
          </div>
        </label>
        {dragActive && (
          <div
            id="drag-file-element"
            onDragEnter={handleDrag}
            onDragLeave={handleDrag}
            onDragOver={handleDrag}
            onDrop={handleDrop}
          ></div>
        )}
        <button type="submit" id="submit-resume">
          {' '}
          Submit
        </button>
      </form>
    </div>
  );
}

export default App;
