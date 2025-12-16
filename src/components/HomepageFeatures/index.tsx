import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type ModuleItem = {
  title: string;
  week: string;
  status: 'Available' | 'Coming Soon';
  description: ReactNode;
  link: string;
};

const ModuleList: ModuleItem[] = [
  {
    title: 'Part I: Foundations',
    week: 'Weeks 1-3',
    status: 'Available',
    description: (
      <>
        Start with the fundamentals of Physical AI, master ROS 2, and build your first production-ready robotic applications.
      </>
    ),
    link: '/docs/Part-I-Foundations/intro',
  },
  {
    title: 'Part II: Digital Twins',
    week: 'Weeks 4-6',
    status: 'Available',
    description: (
      <>
        Learn to model complex robots using URDF and create high-fidelity digital twins in Gazebo for robust testing and simulation.
      </>
    ),
    link: '/docs/Part-II-Digital-Twins/intro',
  },
  {
    title: 'Part III: NVIDIA Isaac',
    week: 'Weeks 7-9',
    status: 'Coming Soon',
    description: (
      <>
        Dive into the NVIDIA Isaac ecosystem for advanced robotics, including GPU-accelerated simulation and AI-powered perception.
      </>
    ),
    link: '/docs/Part-III-NVIDIA-Isaac/intro',
  },
  {
    title: 'Part IV: VLA & Humanoids',
    week: 'Weeks 10-13',
    status: 'Coming Soon',
    description: (
      <>
        Explore the cutting-edge of AI with Vision-Language-Action (VLA) models and tackle the challenges of humanoid locomotion and manipulation.
      </>
    ),
    link: '/docs/Part-IV-VLA-Humanoid/intro',
  },
];

function ModuleCard({title, week, status, description, link}: ModuleItem) {
  return (
    <div className="col col--6 margin-bottom--lg">
      <Link to={link} className={styles.moduleCard}>
        <div className={styles.moduleCardHeader}>
          <Heading as="h3">{title}</Heading>
          <span className={styles.moduleWeek}>{week}</span>
        </div>
        <p>{description}</p>
        <span
          className={clsx(
            styles.moduleStatus,
            status === 'Available' ? styles.isAvailable : styles.isComingSoon
          )}
        >
          {status}
        </span>
      </Link>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="text--center margin-bottom--xl">
          <Heading as="h2">Course Modules</Heading>
          <p>A 13-week curriculum designed for industry practitioners.</p>
        </div>
        <div className="row">
          {ModuleList.map((props, idx) => (
            <ModuleCard key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}