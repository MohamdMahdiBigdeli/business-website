import React from 'react';
import parse from "html-react-parser";
// import About from "../../../data/About/home-two";
import aboutThumb from '../../../assets/img/about-2-bg.jpg'
import { Link } from "react-router-dom";
import axios from 'axios';
import { base_URL } from "../../../helpers/BaseURL"

const About = () => {
  const base_url = base_URL() + "about-data/"
  const [AboutData, setAboutData] = React.useState({
    "title": "",
    "heading": "",
    "since": "",
    "text": "",
    "btnText": "",
    "btnLink": "",
    "thumb": "about-2.jpg"
  })
  React.useEffect(() => {
    axios.get(base_url).then((Response) => {
      setAboutData(Response.data[0])
    })
  })
  
  return (
    <div className="home-two-about-area" style={{ backgroundImage: `url(${aboutThumb})` }}>
      <div className="container">
        <div className="row align-items-center">
          <div className="col-12 d-lg-none">
            <figure className="about-thumb">
              <img src={require('../../../assets/img/' + AboutData.thumb)} alt="Businex-About" />
            </figure>
          </div>

          <div className="col-lg-6">
            <div className="about-content about-content--2">
              <h6>{AboutData.title}</h6>
              <h2>{parse(AboutData.heading)}</h2>
              <span className="about-since">{AboutData.since}</span>
              <p>{parse(AboutData.text)}</p>
              <Link to={`${process.env.PUBLIC_URL + AboutData.btnLink}`} className="btn-about">{AboutData.btnText} <i className="fa fa-angle-double-left" /></Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;