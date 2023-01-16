import React, { Component } from "react";
import Zmage from "react-zmage";
import Fade from "react-awesome-reveal";

let id = 0;
class Portfolio extends Component {
  render() {
    const projects = [
      {
        title: "Iliyas",
        category: "My Travel Blog for my post-university travels",
        image: "01.jpg",
        url: "https://www.canadianwanderlust.com",
      },
      {
        title: "Iliyas",
        category: "My Travel Blog for my post-university travels",
        image: "01.jpg",
        url: "https://www.canadianwanderlust.com",
      },
      {
        title: "Iliyas",
        category: "My Travel Blog for my post-university travels",
        image: "01.jpg",
        url: "https://www.canadianwanderlust.com",
      },
      {
        title: "Iliyas",
        category: "My Travel Blog for my post-university travels",
        image: "01.jpg",
        url: "https://www.canadianwanderlust.com",
      },
    ];
    const project = projects.map(function (project) {
      let projectImage = "images/portfolio/" + project.image;

      return (
        <div key={id++} className="columns portfolio-item">
          <div className="item-wrap">
            <Zmage alt={project.title} src={projectImage} />
            <div style={{ textAlign: "center" }}>{project.title}</div>
            <div style={{ textAlign: "center" }}>{project.title}</div>
          </div>
        </div>
      );
    });

    return (
      <section id="portfolio">
        <Fade left duration={1000} distance="40px">
          <div className="row">
            <div className="twelve columns collapsed">
              <h1>
                HiTalent's
                <br />
                Team
                <br />
              </h1>

              <div
                id="portfolio-wrapper"
                className="bgrid-quarters s-bgrid-thirds cf"
              >
                {project}
              </div>
            </div>
          </div>
        </Fade>
      </section>
    );
  }
}

export default Portfolio;
