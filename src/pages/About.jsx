import { detailedSkills, timelineData } from '../data/skills'
import Timeline from '../components/Timeline'
import SkillBar from '../components/SkillBar'
import './About.css'

function About() {
  const handleResumeDownload = () => {
    // 简历文件应放在 public 文件夹中
    // 如果文件在 public/resume.pdf，则路径为 '/resume.pdf'
    // 或者使用外部链接
    const resumePath = '/resume.pdf' // 请将简历PDF文件放在 public 文件夹中并命名为 resume.pdf
    window.open(resumePath, '_blank')
  }

  return (
    <div className="about-page">
      <div className="container">
        <div className="about-header">
          <h1 className="page-title">关于我</h1>
          <p className="page-subtitle">了解我的背景和技能</p>
        </div>

        <div className="about-content">
          {/* 个人简介 */}
          <div className="about-section">
            <h2 className="section-heading">个人简介</h2>
            <p className="section-text">
              我是彭诗琪，悉尼大学计算机科学硕士在读，具备将数据模型转化为实际产品功能的完整经验。
              我热衷于通过数据驱动的方法解决实际问题，将技术能力与产品思维相结合。
              我的背景涵盖了从数据分析、机器学习到产品管理的多个领域，擅长将复杂的技术转化为用户价值。
            </p>
            <p className="section-text">
              我拥有实际的产品管理工作经验，曾担任AP+AC项目经理，负责产品全生命周期管理。
              同时拥有丰富的项目经验，包括糖尿病风险预测模型、PetCare宠物健康管理平台等，能够基于技术可行性分析驱动产品决策。
            </p>
            <div className="resume-download">
              <button onClick={handleResumeDownload} className="btn-resume">
                📄 下载简历 PDF
              </button>
            </div>
          </div>

          {/* 教育背景 - 时间轴 */}
          <div className="about-section">
            <h2 className="section-heading">教育背景</h2>
            <Timeline items={timelineData} />
          </div>

          {/* 技能图谱 */}
          <div className="about-section">
            <h2 className="section-heading">技能图谱</h2>
            <div className="skills-map">
              {detailedSkills.map((group, groupIndex) => (
                <div key={groupIndex} className="skill-category">
                  <h3 className="skill-category-title">{group.category}</h3>
                  <div className="skill-bars">
                    {group.skills.map((skill, skillIndex) => (
                      <SkillBar
                        key={skillIndex}
                        name={skill.name}
                        proficiency={skill.proficiency}
                      />
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* 工作经历 */}
          <div className="about-section">
            <h2 className="section-heading">工作经历</h2>
            <div className="experience-list">
              <div className="experience-item">
                <div className="experience-icon">💼</div>
                <div className="experience-content">
                  <h3>AP+AC项目经理 | 深圳市云联友科科技有限公司</h3>
                  <p className="experience-period">2023.11 - 2024.06</p>
                  <p>
                    • 产品定义与需求管理：作为对接9家战略客户的核心接口，通过深度访谈与场景分析，精准转化8项核心需求为产品功能方案，并撰写PRD，主导需求评审，最终推动客户续约率提升25%。<br/>
                    • 产品全周期管理与敏捷交付：主导一款商用路由器新品从市场分析、功能定义到量产的全流程，协调硬件、软件、测试等5+部门资源，通过敏捷开发（Scrum）管理迭代，将关键迭代周期平均缩短40%。
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* 联系方式 */}
          <div className="about-section">
            <h2 className="section-heading">联系方式</h2>
            <p className="section-text">
              如果您对我的项目感兴趣，或者想要了解更多信息，欢迎通过以下方式联系我。
            </p>
            <div className="contact-info">
              <p>📧 邮箱: <a href="mailto:pengshiqi42@hotmail.com" style={{ color: 'var(--primary-color)' }}>pengshiqi42@hotmail.com</a></p>
              <p>📱 电话: 15559870708</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default About
