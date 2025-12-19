import { Link } from 'react-router-dom'
import { projects } from '../data/projects'
import { coreSkills } from '../data/skills'
import './Home.css'

function Home() {
  const featuredProjects = projects.slice(0, 4)

  return (
    <div className="home">
      {/* 视觉头图 */}
      <section className="hero">
        <div className="hero-content">
          <div className="hero-intro">
            <h1 className="hero-title">
              彭诗琪
            </h1>
            <p className="hero-subtitle">
              AI数据产品经理 | 计算机科学硕士 | 悉尼大学
            </p>
            <p className="hero-description">
              具备将数据模型转化为实际产品功能的完整经验。擅长通过数据驱动的方法解决实际问题，将技术能力与产品思维相结合，基于技术可行性分析驱动产品决策。
            </p>
          </div>
          
          {/* 核心技能标签 */}
          <div className="core-skills">
            {coreSkills.map((skill, index) => (
              <span key={index} className="core-skill-tag">
                {skill}
              </span>
            ))}
          </div>

          <div className="hero-buttons">
            <Link to="/about" className="btn btn-primary">
              了解更多
            </Link>
            <Link to="/projects" className="btn btn-secondary">
              查看项目
            </Link>
          </div>
        </div>
      </section>

      {/* 精选项目 */}
      <section className="featured-projects">
        <div className="container">
          <h2 className="section-title">精选项目</h2>
          <div className="projects-grid">
            {featuredProjects.map((project) => (
              <Link 
                key={project.id} 
                to="/projects" 
                className="project-card"
              >
                <div className="project-image">
                  {project.image ? (
                    <img 
                      src={project.image} 
                      alt={project.title}
                      className="project-image-img"
                    />
                  ) : (
                    <div className="project-placeholder">
                      {project.title.charAt(0)}
                    </div>
                  )}
                </div>
                <div className="project-content">
                  <span className="project-category">{project.category}</span>
                  <h3 className="project-title">{project.title}</h3>
                  <p className="project-description">{project.description}</p>
                  <div className="project-highlight">
                    <span className="highlight-icon">✨</span>
                    <span>{project.features[0]}</span>
                  </div>
                  <div className="project-tech">
                    {project.technologies.slice(0, 3).map((tech, idx) => (
                      <span key={idx} className="tech-tag">{tech}</span>
                    ))}
                  </div>
                </div>
              </Link>
            ))}
          </div>
          <div className="view-all">
            <Link to="/projects" className="btn btn-outline">
              查看所有项目 →
            </Link>
          </div>
        </div>
      </section>

    </div>
  )
}

export default Home
