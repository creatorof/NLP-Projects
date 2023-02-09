import './App.css';
import React from 'react';
import { useState } from 'react';
import paperLogo from './paper-icon.png';
import axios from 'axios';

function App() {
  // drag state
  const [dragActive, setDragActive] = useState(false);
  const [uploaded, setUploaded] = useState(false);
  // ref
  const inputRef = React.useRef(null);
  //const [showDownloadButton, setShowDownloadButton] = useState(false);
  const [resumes, setResumes] = useState([]);
  const [displayList, setDisplayList] = useState(false);
  const [back, setBack] = useState(false);
  const [education, setEducation] = useState([]);
  const [skills, setSkills] = useState([]);

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
    uploadResume(e.dataTransfer.files);
  };

  // triggers when file is selected with click
  const handleChange = function (e) {
    e.preventDefault();
    uploadResume(e.target.files);
  };

  const uploadResume = function (resume) {
    if (resume && resume.length >= 1) {
      resume = resume[0];
      setResumes(resume);
      setUploaded(true);
    }
  };

  // triggers the input when the button is clicked
  const onButtonClick = () => {
    inputRef.current.click();
  };

  const onSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', resumes);

    //setShowDownloadButton(true);
    axios
      .post('http://127.0.0.1:5000/upload_resume', formData, {
        headers: {
          'Content-Type': resumes.type,
        },
      })
      .then((res) => {
        console.log(res.data);
        setDisplayList(true);
        setEducation(res.data.education);
        setSkills(res.data.skills);
        // const skills = res.data.skills.filter(
        //   (item, i, skills) => skills.indexOf(item) === i
        // );
        // setSkillsList(skills);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const goBack = () => {
    setDisplayList(false);
    setUploaded(false);
  };

  return (
    <>
      {displayList ? (
        <>
          <div>
            <button className="back-btn upload-button" onClick={goBack}>
              {'<<'}Go Back
            </button>
          </div>
          <div className="grid-container list-div">
            <div className="grid-item">
              <h2>Education</h2>
              <ol className="education-list">
                {education &&
                  education.map((ed) => (
                    <li className={`${ed} list-item`}>{ed}</li>
                  ))}
              </ol>
            </div>
            <div className="grid-item">
              <h2>Skills</h2>
              <ol className="skill-list">
                {skills &&
                  skills.map((skill) => (
                    <li className={`${skill} list-item`}>{skill}</li>
                  ))}
              </ol>
            </div>
          </div>
        </>
      ) : (
        <div className="page">
          <form
            id="form-file-upload"
            onSubmit={(e) => e.preventDefault()}
            onDragEnter={handleDrag}
          >
            <input
              ref={inputRef}
              type="file"
              id="input-file-upload"
              accept=".pdf"
              onChange={handleChange}
            />
            <label
              id="label-file-upload"
              htmlFor="input-file-upload"
              className={dragActive ? 'drag-active' : ''}
            >
              {uploaded ? (
                <div className="parse-resume-div">
                  <img src={paperLogo} height={100} width={100}></img>
                  <p className="text">{resumes.name}</p>
                  <button type="button" id="submit-resume" onClick={onSubmit}>
                    Parse resume
                  </button>
                  <h6 className="h6-text">OR</h6>
                  <button className="upload-button" onClick={onButtonClick}>
                    Choose a different one
                  </button>
                </div>
              ) : (
                <div>
                  <p>Drag and drop your resume here or</p>
                  <button className="upload-button" onClick={onButtonClick}>
                    Upload a Resume
                  </button>
                </div>
              )}
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
          </form>
        </div>
      )}
    </>
  );
}

export default App;
