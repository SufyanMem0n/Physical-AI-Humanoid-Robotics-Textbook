import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

/**
 * Define the sidebars for the course documentation.
 */
const sidebars: SidebarsConfig = {
  // We explicitly define the sidebar structure to match the course modules.
  courseSidebar: [
    'intro', // The main landing page
    {
      type: 'category',
      label: 'Part I: Foundations',
      link: {
        type: 'doc',
        id: 'Part-I-Foundations/intro',
      },
      items: [
        'Part-I-Foundations/ROS-2/intro',
      ],
    },
    {
      type: 'category',
      label: 'Part II: Digital Twins',
      link: {
        type: 'doc',
        id: 'Part-II-Digital-Twins/intro',
      },
      items: [
        'Part-II-Digital-Twins/Gazebo/intro',
      ],
    },
    {
      type: 'category',
      label: 'Part III: NVIDIA Isaac',
      link: {
        type: 'doc',
        id: 'Part-III-NVIDIA-Isaac/intro',
      },
      items: [
        'Part-III-NVIDIA-Isaac/Isaac-Sim/intro',
      ],
    },
    {
      type: 'category',
      label: 'Part IV: VLA & Humanoid Robotics',
      link: {
        type: 'doc',
        id: 'Part-IV-VLA-Humanoid/intro',
      },
      items: [
        'Part-IV-VLA-Humanoid/VLA/intro',
      ],
    },
  ],
};

export default sidebars;
