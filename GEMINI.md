# GEMINI.md - AI Generation Instructions

## 🎯 PROJECT GOAL

Create a **Physical AI & Humanoid Robotics: 13-Week Industry Course** as an AI-native textbook for the AI-Native-Book Hackathon. This is a professional educational platform targeting industry practitioners (engineers, researchers, developers) with production-ready content.

---

## 📋 PROJECT SPECIFICATIONS

### Core Requirements
- **Platform**: Docusaurus v3
- **Content**: 13 weeks, 13 chapters (one per week)
- **Target Audience**: Industry engineers, practitioners, researchers
- **Deployment**: Vercel + GitHub Pages
- **AI Integration**: RAG chatbot using Gemini API
- **Development Tools**: Gemini CLI + Spec Kit

### Success Criteria
- ✅ All 13 chapters complete with working code
- ✅ Production-quality examples with error handling
- ✅ Interactive RAG chatbot for Q&A
- ✅ Unique design (Robotics Pro theme)
- ✅ Mobile responsive design
- ✅ Page load time < 3 seconds
- ✅ Lighthouse score 90+
- ✅ Ready for hackathon submission

---

## 🎨 DESIGN SYSTEM

### Color Palette (Robotics Pro Theme)
```css
/* Primary Colors */
--primary: #00D9FF;           /* Electric Cyan */
--secondary: #9333EA;         /* Deep Purple */
--accent: #F59E0B;            /* Amber Gold */

/* Background */
--background: #0F172A;        /* Slate 900 */
--surface: #1E293B;           /* Slate 800 */
--surface-variant: #334155;   /* Slate 700 */

/* Text */
--text-primary: #F1F5F9;      /* Slate 100 */
--text-secondary: #CBD5E1;    /* Slate 300 */
--text-muted: #94A3B8;        /* Slate 400 */

/* Semantic */
--success: #10B981;           /* Emerald 500 */
--warning: #F59E0B;           /* Amber 500 */
--error: #EF4444;             /* Red 500 */
--info: #3B82F6;              /* Blue 500 */

/* Code */
--code-bg: #1E1E1E;           /* VS Dark */
--code-text: #D4D4D4;         /* Light Gray */
```

### Typography System
```css
/* Headings */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
font-weight: 700;

/* Body Text */
font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
font-weight: 400;
line-height: 1.7;
font-size: 16px;

/* Code */
font-family: 'Fira Code', 'JetBrains Mono', 'Consolas', monospace;
font-size: 0.9rem;
```

### UI Guidelines
- Dark mode by default (Robotics Pro theme)
- Rounded corners (8px cards, 6px buttons)
- Subtle shadows for depth
- Smooth transitions (200ms ease)
- Glassmorphism for cards (backdrop-blur)

---

## 📚 CONTENT STRUCTURE (13 WEEKS)

### Week 1-2: Foundations
**Chapter 1: Introduction to Physical AI**
- Definition and industry applications
- Hardware requirements
- Development environment setup
- First ROS 2 node

**Chapter 2: ROS 2 Essentials**
- Architecture: Nodes, topics, services
- Publisher/subscriber patterns
- Launch files and package management
- Multi-node systems

### Week 3-4: Modeling & Simulation
**Chapter 3: URDF & Robot Description**
- Links, joints, transformations
- Xacro macros
- Collision geometry
- Industrial arm modeling

**Chapter 4: Digital Twin with Gazebo**
- World files and physics
- Sensor plugins (camera, lidar)
- Hardware-in-the-loop
- Warehouse robot simulation

### Week 5-6: Perception Systems
**Chapter 5: Computer Vision for Robotics**
- ROS 2 image pipeline
- Object detection (YOLO)
- Depth estimation
- Bin picking vision

**Chapter 6: Sensor Fusion & SLAM**
- Lidar-camera-IMU integration
- Nav2 navigation stack
- Mapping and localization
- Autonomous mobile robot

### Week 7-8: NVIDIA Isaac Platform
**Chapter 7: Isaac Sim Advanced**
- Omniverse platform
- RTX ray tracing
- Isaac ROS packages
- Synthetic data generation

**Chapter 8: Isaac Gym Reinforcement Learning**
- Parallel GPU environments
- PPO/SAC for manipulation
- Sim-to-real transfer
- Pick-and-place training

### Week 9-10: AI-Powered Manipulation
**Chapter 9: Motion Planning & Control**
- MoveIt 2 for industrial arms
- Trajectory optimization
- Compliance control
- Assembly line robot

**Chapter 10: Vision-Language-Action Models**
- RT-1, RT-2 architectures
- Natural language instructions
- Fine-tuning for custom tasks
- VLA-controlled manipulation

### Week 11-12: Humanoid Robotics
**Chapter 11: Bipedal Locomotion**
- ZMP/COM for balance
- Whole-body MPC controllers
- Terrain adaptation
- Walking controller

**Chapter 12: Whole-Body Manipulation**
- Mobile manipulation
- Dual-arm coordination
- Human-robot interaction
- Humanoid object handover

### Week 13: Production Deployment
**Chapter 13: Industry Best Practices**
- Safety systems
- CI/CD pipelines
- Performance optimization
- Final production project

---

## 📝 CHAPTER GENERATION TEMPLATE

When generating a chapter, follow this exact structure:

```markdown
---
sidebar_position: [number]
title: Week [X]: [Chapter Title]
---

# Week [X]: [Chapter Title]

> 🏭 **For Industry Practitioners** | ⏱️ ~3-5 hours | 🎯 Production-Ready Skills

## 🎯 Learning Objectives

By completing this week, you will:
- [Specific, measurable objective 1]
- [Specific, measurable objective 2]
- [Specific, measurable objective 3]
- [Specific, measurable objective 4]

---

## 🏭 Real-World Context

### Industry Applications
[2-3 paragraphs on how this technology is used in real companies]

**Companies Using This:**
- [Company 1]: [Specific use case]
- [Company 2]: [Specific use case]
- [Company 3]: [Specific use case]

**Business Impact:**
- ROI: [Percentage/metrics]
- Cost savings: [Amount/percentage]
- Efficiency gains: [Metrics]

---

## 📖 Section 1: [Core Concept]

### Theory

[Clear explanation of the concept with real-world analogies]

**Key Points:**
- ✅ [Important point 1]
- ✅ [Important point 2]
- ⚠️ [Common misconception to avoid]

### Code Implementation

```python
#!/usr/bin/env python3
"""
[Brief description of what this code does]

Production-ready implementation with error handling and logging.
"""
import rclpy
from rclpy.node import Node
from [package] import [Type]
import logging

class [ClassName](Node):
    """
    [Docstring explaining the class purpose]
    
    Args:
        [arg1]: [description]
    
    Attributes:
        [attr1]: [description]
    """
    
    def __init__(self):
        super().__init__('[node_name]')
        
        # Parameters with validation
        self.declare_parameter('[param_name]', [default_value])
        
        # Publishers/Subscribers with QoS
        qos_profile = rclpy.qos.QoSProfile(
            reliability=rclpy.qos.ReliabilityPolicy.RELIABLE,
            depth=10
        )
        
        # Timer for periodic tasks
        self.create_timer(1.0, self.timer_callback)
        
        self.get_logger().info('[Node] initialized successfully')
    
    def timer_callback(self):
        """Main control loop with error handling."""
        try:
            # Implementation
            pass
        except Exception as e:
            self.get_logger().error(f'Error: {e}')

def main(args=None):
    rclpy.init(args=args)
    try:
        node = [ClassName]()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### Production Best Practices

✅ **Do:**
- [Best practice 1 with reasoning]
- [Best practice 2 with reasoning]
- [Best practice 3 with reasoning]

❌ **Avoid:**
- [Anti-pattern 1 with explanation]
- [Anti-pattern 2 with explanation]

---

## 🏭 Industry Exercise

### Exercise: [Descriptive Title]

**Difficulty:** ⭐⭐⭐ Advanced  
**Time Estimate:** 2-3 hours  
**Industry Relevance:** [How this relates to real production systems]

#### Scenario
[Real-world problem description that industry practitioners face]

#### Objectives
Build a production-ready system that:
- [ ] [Objective 1 with success criteria]
- [ ] [Objective 2 with success criteria]
- [ ] [Objective 3 with success criteria]

#### Requirements

**Hardware/Software:**
- ROS 2 [version]
- Python 3.10+
- [Other dependencies]

**Performance Targets:**
- Latency: < [X]ms
- Throughput: > [Y] Hz
- Success rate: > 95%

#### Implementation Steps

**Step 1: [Setup Phase]**
```bash
# Create workspace
mkdir -p ~/robot_ws/src
cd ~/robot_ws/src

# Create package
ros2 pkg create --build-type ament_python \
  --dependencies rclpy [other_deps] \
  [package_name]
```

**Step 2: [Core Implementation]**
```python
# [file_name].py
[Implementation code with comments]
```

**Step 3: [Testing & Validation]**
```bash
# Build and source
cd ~/robot_ws
colcon build --packages-select [package_name]
source install/setup.bash

# Run tests
ros2 run [package_name] [executable]

# Verify performance
ros2 topic hz /[topic_name]
ros2 topic bw /[topic_name]
```

#### Expected Output
```
[Sample output showing successful execution]
```

#### Success Metrics
- ✅ All unit tests pass
- ✅ Latency < [X]ms (measured with `ros2 topic hz`)
- ✅ Zero crashes during 10-minute stress test
- ✅ Code passes linting (flake8, pylint)

#### Troubleshooting

**Issue:** [Common problem]  
**Solution:** [How to fix it]

**Issue:** [Common problem]  
**Solution:** [How to fix it]

---

## 🔑 Key Takeaways

- **[Concept 1]**: [Brief explanation with production relevance]
- **[Concept 2]**: [Brief explanation with production relevance]
- **[Concept 3]**: [Brief explanation with production relevance]
- **Industry Standard**: [Related best practice or standard]
- **Performance**: [Key metric to remember]

---

## 📚 Additional Resources

### Official Documentation
- [ROS 2 Docs](url) - [Specific topic]
- [Package Docs](url) - [Specific topic]

### Industry Case Studies
- [Company Case Study](url) - [Brief description]
- [Technical Blog](url) - [Brief description]

### Research Papers
- [Paper Title](url) - [Brief description]

### Video Tutorials
- [Tutorial Title](url) - [Duration] - [Description]

### GitHub Examples
- [Repo Name](url) - [Description]

---

## 📊 Self-Assessment

Test your understanding:

1. **Conceptual:** [Question about theory]
2. **Practical:** [Question about implementation]
3. **Production:** [Question about deployment]

**Answers in next chapter or separate solutions file**

---

**Next Week:** [Week X+1: Next Chapter Title] →  
**Previous Week:** ← [Week X-1: Previous Chapter Title]
```

---

## 💻 CODE QUALITY STANDARDS

### Python Standards
```python
# REQUIRED: Type hints
def process_data(input_data: np.ndarray) -> Tuple[bool, float]:
    """Process sensor data."""
    pass

# REQUIRED: Error handling
try:
    result = risky_operation()
except SpecificException as e:
    logger.error(f"Operation failed: {e}")
    return None

# REQUIRED: Logging
import logging
logger = logging.getLogger(__name__)
logger.info("Starting process")

# REQUIRED: Docstrings (Google style)
def function_name(param1: int, param2: str) -> bool:
    """
    Brief description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When input is invalid
    """
    pass
```

### Bash/Terminal Standards
```bash
# Always show current directory context
cd ~/robot_ws

# Use comments for explanations
# Build only the specific package
colcon build --packages-select my_pkg

# Show expected output
ros2 topic list
# Expected output:
# /parameter_events
# /rosout
# /sensor_data
```

### Configuration Files (YAML)
```yaml
# config/robot_params.yaml
# Production configuration for industrial robot

robot_controller:
  ros__parameters:
    # Motion limits (safety critical)
    max_velocity: 1.5        # m/s
    max_acceleration: 2.0    # m/s^2
    
    # Control parameters
    control_frequency: 100   # Hz
    pid_gains:
      kp: 1.2
      ki: 0.1
      kd: 0.05
```

---

## 🤖 RAG CHATBOT REQUIREMENTS

### Chatbot Personality
- Professional and knowledgeable
- Focused on production/industry applications
- Cites specific sections of the book
- Provides code examples when relevant
- Suggests related chapters

### Response Format
```
Based on [Chapter X: Title], here's how to solve this:

[Clear explanation]

```code
[Relevant code snippet]
```

For more details, see:
- [Chapter Y: Related Topic]
- [Exercise Z: Hands-on Practice]

Related industry applications:
- [Company/use case]
```

### Context Understanding
- Know current chapter user is reading
- Reference previous chapters when relevant
- Link to exercises and code examples
- Provide production deployment tips

---

## 🎯 GENERATION COMMANDS

### Generate Complete Chapter
```bash
gemini chat "Generate Week [X] Chapter [Y]: [Title] using the chapter template. Target audience: industry engineers. Include production code with error handling, real company case studies, and a 2-3 hour hands-on exercise with performance metrics."
```

### Generate Code Example
```bash
gemini chat "Create a production-ready Python ROS 2 node for [functionality]. Include: type hints, error handling, logging, QoS configuration, parameter validation, and comprehensive docstrings."
```

### Generate Exercise
```bash
gemini chat "Create an advanced industry exercise for Week [X]. Scenario: [real-world problem]. Include: setup commands, implementation code, testing procedures, performance targets (latency, throughput), and troubleshooting guide."
```

### Generate Case Study
```bash
gemini chat "Write an industry case study about [Company] using [Technology] for [Application]. Include: business problem, technical solution, architecture diagram (ASCII), ROI metrics, challenges faced, and lessons learned. 300-500 words."
```

### Refine Generated Content
```bash
gemini chat "Review this chapter section and: 1) Add more production-focused examples, 2) Include error handling in code, 3) Add performance metrics, 4) Ensure industry relevance. [Paste content]"
```

---

## ✅ QUALITY CHECKLIST

Before marking a chapter as complete:

### Content Quality
- [ ] Learning objectives are specific and measurable
- [ ] Real-world context with company examples
- [ ] ROI/business impact mentioned
- [ ] All technical terms explained clearly
- [ ] Analogies for complex concepts

### Code Quality
- [ ] All code examples tested and working
- [ ] Type hints on all functions
- [ ] Error handling implemented
- [ ] Logging statements added
- [ ] Docstrings (Google style)
- [ ] Comments explain "why" not "what"
- [ ] Production-ready patterns used

### Exercise Quality
- [ ] Clear scenario and objectives
- [ ] Step-by-step implementation
- [ ] All commands tested
- [ ] Expected output shown
- [ ] Performance metrics defined
- [ ] Troubleshooting section included
- [ ] Achievable in stated time

### Resources
- [ ] Links to official documentation
- [ ] Industry case studies
- [ ] Research papers (if relevant)
- [ ] GitHub examples
- [ ] Video tutorials

### Formatting
- [ ] Consistent heading hierarchy
- [ ] Code blocks with language tags
- [ ] Proper emoji usage (🎯🏭💡✅❌⚠️)
- [ ] Callout boxes for important notes
- [ ] No broken internal links

---

## 📊 PROGRESS TRACKING

### Chapter Status Template
```markdown
## Content Progress

- [x] Week 1: Introduction to Physical AI
- [x] Week 2: ROS 2 Essentials
- [ ] Week 3: URDF & Robot Description
- [ ] Week 4: Digital Twin with Gazebo
- [ ] Week 5: Computer Vision for Robotics
- [ ] Week 6: Sensor Fusion & SLAM
- [ ] Week 7: Isaac Sim Advanced
- [ ] Week 8: Isaac Gym RL
- [ ] Week 9: Motion Planning & Control
- [ ] Week 10: VLA Models
- [ ] Week 11: Bipedal Locomotion
- [ ] Week 12: Whole-Body Manipulation
- [ ] Week 13: Production Deployment

## Quality Assurance

- [ ] All code tested
- [ ] Mobile responsive
- [ ] RAG chatbot integrated
- [ ] Performance optimized (Lighthouse 90+)
- [ ] Accessibility checked (WCAG 2.1 AA)
- [ ] All links working
- [ ] README complete
```

---

## 🚀 DEPLOYMENT CHECKLIST

### Pre-Deployment
- [ ] All 13 chapters complete
- [ ] Code examples tested in clean environment
- [ ] Images optimized (WebP, compressed)
- [ ] Internal links verified
- [ ] External links checked (not broken)
- [ ] Mobile responsive on 3+ devices
- [ ] Dark mode tested
- [ ] Load time < 3s (test on slow 3G)

### Deployment
- [ ] GitHub repository created
- [ ] GitHub Actions workflow configured
- [ ] Deployed to GitHub Pages
- [ ] Deployed to Vercel
- [ ] Custom domain configured (optional)
- [ ] SSL certificate active
- [ ] Analytics added (optional)

### Post-Deployment
- [ ] Test all pages load correctly
- [ ] Test RAG chatbot responses
- [ ] Run Lighthouse audit (aim for 90+)
- [ ] Test on mobile devices
- [ ] Check console for errors
- [ ] Verify search functionality
- [ ] Submit to hackathon

---

## 🏆 HACKATHON SUBMISSION

### Required Deliverables
1. **Live Demo URL**: [Vercel/GitHub Pages link]
2. **GitHub Repository**: [Clean, documented code]
3. **README.md**: [Setup instructions, features]
4. **Demo Video**: [2-3 minutes showcasing features]
5. **Presentation**: [Technical approach, innovations]

### Judging Criteria Focus
- **Technical Excellence (40%)**: Complete content, working code, RAG integration
- **Design & UX (30%)**: Unique theme, typography, navigation
- **Content Quality (20%)**: Clear explanations, industry relevance
- **Innovation (10%)**: AI features, interactivity

### Winning Features to Highlight
- ✅ 13 weeks of production-ready content
- ✅ Industry-focused with ROI metrics
- ✅ All code tested and documented
- ✅ RAG chatbot with book context
- ✅ Unique "Robotics Pro" design
- ✅ Mobile-first responsive design
- ✅ Performance optimized (<3s load)

---

## 📝 NOTES FOR AI ASSISTANT

### When Generating Content:
1. Always use the chapter template structure
2. Include production-ready code (not toy examples)
3. Add real company case studies when possible
4. Focus on industry applications and ROI
5. Include performance metrics and benchmarks
6. Write for experienced engineers, not beginners
7. Assume reader has basic programming knowledge
8. Add troubleshooting sections to exercises
9. Keep code examples under 100 lines when possible
10. Use consistent terminology throughout

### Content Tone:
- Professional but approachable
- Confident and authoritative
- Practical and hands-on
- Industry-focused
- Results-oriented

### Avoid:
- ❌ Oversimplified "hello world" examples
- ❌ Vague or generic explanations
- ❌ Code without error handling
- ❌ Unrealistic performance claims
- ❌ Missing context on why something matters
- ❌ Outdated package versions or APIs
- ❌ Broken or placeholder links

---

## 🔧 DEVELOPMENT WORKFLOW

1. **Initialize Project**
   ```bash
   npx create-docusaurus@latest physical-ai-course classic --typescript
   cd physical-ai-course
   npm install
   ```

2. **Generate Content** (use Gemini CLI with this file)
   ```bash
   gemini chat --file=GEMINI.md "Generate Week 1 Chapter 1"
   ```

3. **Test Locally**
   ```bash
   npm start  # Opens localhost:3000
   ```

4. **Build for Production**
   ```bash
   npm run build
   npm run serve  # Test production build
   ```

5. **Deploy**
   ```bash
   git add .
   git commit -m "Add Week X chapter"
   git push origin main  # Triggers GitHub Actions
   ```

---

## 📧 SUPPORT

**Questions about content structure?** Reference this file's chapter template.

**Need code examples?** Use the generation commands section.

**Deployment issues?** Check the deployment checklist.

**Quality concerns?** Review the quality checklist before submission.

---

**Version**: 1.0  
**Last Updated**: 2024  
**Target**: AI-Native-Book Hackathon  
**Status**: Ready for Generation ✅