import './Timeline.css'

function Timeline({ items }) {
  return (
    <div className="timeline">
      {items.map((item, index) => (
        <div key={index} className="timeline-item">
          <div className="timeline-marker" />
          <div className="timeline-content">
            <div className="timeline-date">{item.date}</div>
            <h3 className="timeline-title">{item.title}</h3>
            {item.subtitle && (
              <p className="timeline-subtitle">{item.subtitle}</p>
            )}
            <p className="timeline-description">{item.description}</p>
            {item.courses && (
              <div className="timeline-courses">
                <h4 className="courses-title">相关课程</h4>
                <ul className="course-list">
                  {item.courses.map((course, courseIndex) => (
                    <li key={courseIndex}>{course}</li>
                  ))}
                </ul>
              </div>
            )}
            {item.tags && (
              <div className="timeline-tags">
                {item.tags.map((tag, tagIndex) => (
                  <span key={tagIndex} className="timeline-tag">
                    {tag}
                  </span>
                ))}
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  )
}

export default Timeline





