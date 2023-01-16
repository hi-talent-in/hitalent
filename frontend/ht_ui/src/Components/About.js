import React, { Component } from "react";
import Fade from "react-awesome-reveal";

class About extends Component {
  render() {
    return (
      <section id="about">
        <Fade duration={1000}>
          <div className="row">
            <div className="nine columns main-col">
              <h2>About Us</h2>
              <p>
                Hi Talent is an online programming training platform that is on
                a mission to help students learn programming{" "}
                <strong>free of cost</strong>. We deliver our training through
                internship of 3-6 months duration and apprenticeship of 6-9
                months duration, which equips the talents with necessary
                programming skills. Our end goal is that after the internship or
                apprenticeship, the talent will be able to get a job as sotware
                developer. With us, the talents have a chance to try their hands
                on live projects, which give them actual industry exposure. We
                are sure that our training programs helps the talents to update
                their programming skills according to current industry
                standards. We are delivering training in Java, Python,
                Javascript, DotNet, SQL, Docker, DevOps, Agile, Algorithms and
                basic data structure.
              </p>
            </div>
          </div>
        </Fade>
      </section>
    );
  }
}

export default About;
