import React, { useEffect } from "react";
import { Fade } from "react-awesome-reveal";
import { useNavigate, useLocation } from "react-router-dom";
import axios from "axios";
import About from "./About";
import Resume from "./Resume";
import Footer from "./Footer";
import Portfolio from "./Portfolio";
import Contact from "./Contact";
import Testimonials from "./Testimonials";

const Header = (props) => {
  const router = useNavigate();
  const location = useLocation();
  var searchParams = new URLSearchParams(location.search);
  useEffect(() => {
    async function googleLogin() {
      const code = searchParams.get("code");
      if (searchParams.has("code")) {
        try {
          await axios
            .post(
              "http://localhost:8000/intern/google/tokens/",
              { code: code },
              { headers: { "Content-Type": "application/json" } }
            )
            .then((res) => {
              console.log("res", res);
              if (res.status === 200) {
                sessionStorage?.setItem("token", res?.data?.tokens?.access);
                sessionStorage.setItem("refresh", res?.data?.tokens?.refresh);
                // getAllUsers();
              }
            });
        } catch {
          router("/");
        }
      } else {
        const login = sessionStorage.getItem("token");
        if (!login) {
          router("/");
        } else {
          // getAllUsers();
        }
      }
    }
    googleLogin();
  }, []);
  return (
    <>
      <header id="home">
        <nav id="nav-wrap">
          <a className="mobile-btn" href="#nav-wrap" title="Show navigation">
            Show navigation
          </a>
          <a className="mobile-btn" href="#home" title="Hide navigation">
            Hide navigation
          </a>

          <ul id="nav" className="nav">
            <li className="current">
              <a className="smoothscroll" href="#home">
                Home
              </a>
            </li>

            <li>
              <a className="smoothscroll" href="#about">
                About
              </a>
            </li>
            <li>
              <a className="smoothscroll" href="#resume">
                Programs
              </a>
            </li>
            <li>
              <a className="smoothscroll" href="#portfolio">
                Team
              </a>
            </li>
            <li>
              <a className="smoothscroll" href="#contact">
                Contact
              </a>
            </li>
          </ul>
        </nav>

        <div className="row banner">
          <div className="banner-text">
            <Fade bottom>
              <h1 className="responsive-headline">HiTalent</h1>
            </Fade>
            <Fade bottom duration={1200}>
              <h3>Get Skilled Here.</h3>
            </Fade>
            <hr />
            <Fade bottom duration={2000}>
              <ul className="social">
                <a
                  href="https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=http%3A%2F%2Flocalhost%3A3000&prompt=consent&response_type=code&client_id=917537609153-lpfjkd2e0ca4otak7focgqs1mbv7g2ut.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow"
                  className="button btn project-btn"
                >
                  Intern With Us
                </a>
                <a
                  href="https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=http%3A%2F%2Flocalhost%3A3000&prompt=consent&response_type=code&client_id=917537609153-lpfjkd2e0ca4otak7focgqs1mbv7g2ut.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow"
                  className="button btn github-btn"
                >
                  Currently Intern
                </a>
              </ul>
            </Fade>
          </div>
        </div>

        <p className="scrolldown">
          <a className="smoothscroll" href="#about">
            <i className="icon-down-circle"></i>
          </a>
        </p>
      </header>
      <About />
      <Resume />
      <Testimonials />
      <Portfolio />
      <Contact />
      <Footer />
    </>
  );
};

export default Header;
