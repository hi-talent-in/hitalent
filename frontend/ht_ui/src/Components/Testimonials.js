import React from 'react'

const Testimonials = () => {
  const testimonials = [
    {
      user: "Iliyas(Zelhus Consultants)",
      text: "I did 3 months internship and then I got placed in a company where I'm working on big time real life projects.",
    },
    {
      user: "Meraa(Google)",
      text: "At first I didn't has any prior programming knowledge but with apprentice program I have got enough skills to be placed in largest Tech company and for this I will be thankful to madan",
    },
  ];
  // if (!this.props.data) return null;
  const testimonial = testimonials.map(function (testimonial) {
    return (
      <li key={testimonial.user}>
        <blockquote>
          <p>{testimonial.text}</p>
          <cite>{testimonial.user}</cite>
        </blockquote>
      </li>
    );
  });
  return (
    <section id="testimonials">
      <div className="text-container">
        <div className="row">
          <div className="two columns header-col">
            <h1>
              <span>Client Testimonials</span>
            </h1>
          </div>

          <div className="ten columns flex-container">
            <ul className="slides">{testimonial}</ul>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Testimonials