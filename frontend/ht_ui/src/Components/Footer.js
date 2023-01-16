import React, { Component } from "react";
import Fade from "react-awesome-reveal";

class Footer extends Component {
  render() {
    const main = {
      social: [
        {
          name: "linkedin",
          url: "https://www.linkedin.com/in/mmmiitr/",
          className: "fa fa-linkedin",
        },
        {
          name: "github",
          url: "https://github.com/hi-talent-org/hitalent",
          className: "fa fa-github",
        },
      ],
    };
    const networks = main.social.map(function (network) {
      return (
        <li key={network.name}>
          <a href={network.url}>
            <i className={network.className}></i>
          </a>
        </li>
      );
    });

    return (
      <footer>
        <div className="row">
          <Fade bottom>
            <div className="twelve columns">
              <ul className="social-links">{networks}</ul>

              <ul className="copyright">
                <li>&copy; Copyright 2023 HiTalent</li>
                <li>
                  Design by{" "}
                  <a title="Styleshout" href="/about">
                    Iliyas
                  </a>
                </li>
              </ul>
            </div>
          </Fade>

          <div id="go-top">
            <a className="smoothscroll" title="Back to Top" href="#home">
              <i className="icon-up-open"></i>
            </a>
          </div>
        </div>
      </footer>
    );
  }
}

export default Footer;
