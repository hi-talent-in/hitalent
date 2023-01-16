import React, { Component } from "react";
import Slide from "react-awesome-reveal";

class Resume extends Component {
  getRandomColor() {
    let letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  render() {



    return (
      <section id="resume">
        <Slide left duration={1300}>
          <div className="row education">
            <div className="three columns header-col">
              <h1>
                <span>Programs</span>
              </h1>
            </div>

            <div className="nine columns main-col">
              <div className="row item">
                <div className="twelve columns">
                  <h3>Internship Program </h3>
                  <p className="info">(3-6 Months)</p>
                  <p>
                    This program is for candidates who are from the computer
                    science discipline. The entire duration of the program is 3
                    to 6 months in which they are trained on our carriculum and
                    on live projects for which they are provided with a stipend.
                    Our industry oriented carriculum helps them to brush up
                    their basic programming skills and working on live projects
                    gives them necessary industry exposure.
                  </p>
                </div>
                <div className="twelve columns">
                  <h3>Apprenticeship Program</h3>
                  <p className="info">(6-9 Months)</p>
                  <p>
                    This program is for people who are not from computer science
                    discipline. People who wish to switch to this field or have
                    a desire to learn computer programming can apply for this
                    program. The entire duration of the program is 6 to 9 months
                    in which they are trained on basic as well as advanced
                    concepts in programming and also have the chance to work on
                    live projects for which they are provided with a stipend.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </Slide>
      </section>
    );
  }
}

export default Resume;
