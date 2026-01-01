# Personal Learning Dashboard (PLD)

A responsive, modern web application for tracking learning progress, managing profiles, and showcasing achievements.

## 🚀 Project Overview

The Personal Learning Dashboard is a UI-focused web application built with HTML5, CSS3 (Tailwind CSS), and vanilla JavaScript. It provides an intuitive interface for students to monitor their learning journey across multiple modules, units, and topics.

## 🛠️ Tech Stack

- **HTML5** - Semantic markup structure
- **Tailwind CSS** - Utility-first CSS framework (via CDN)
- **JavaScript** - Interactive collapsible modules and mobile navigation
- **Responsive Design** - Mobile-first approach

## ✨ Features

### 1. Login Page (`login.html`)
- Clean, centered login form
- Form validation with HTML5
- Responsive design for all screen sizes
- Remember me checkbox
- Forgot password link

### 2. Dashboard (`dashboard.html`)
- **Progress Overview** - Visual stats cards showing labs completed, current module, and completion rate
- **Learning Modules** - Collapsible module cards with:
  - Module → Unit → Topic hierarchy
  - Status badges (Completed, In Progress, Not Started)
  - Progress indicators for each topic
- **Recent Labs** - List of recently completed labs
- **Sticky Header** - Navigation stays visible on scroll
- **Responsive Grid** - Adapts from 1 to 3 columns based on screen size

### 3. Profile Page (`profile.html`)
- **Profile Card** - Avatar, user info, and photo upload
- **Personal Information Form** - Tailwind-styled inputs with:
  - Full Name, Email, Phone
  - Education Level dropdown
  - GitHub Profile link
  - Skills tags/badges
  - Bio textarea
- **Learning Statistics** - Grid of key metrics
- **Responsive Layout** - 2-column form on desktop, single column on mobile

### 4. Gallery (`gallery.html`)
- **Responsive Grid Layout** - 1/2/3 columns (mobile/tablet/desktop)
- **Category Sections**:
  - Projects
  - Certificates
  - Events
  - Achievements
- **Hover Effects** - Cards lift and expand shadow on hover
- **Filter & Sort Controls** - Dropdown selectors
- **Action Buttons** - View, Edit, Delete, Share options
- **Gallery Stats** - 6-column stats grid

## 📱 Responsive Design Strategy

### Breakpoints (Tailwind defaults)
- **Mobile**: < 768px (default)
- **Tablet**: ≥ 768px (`md:`)
- **Desktop**: ≥ 1024px (`lg:`)

### Mobile-First Approach
1. Base styles target mobile devices
2. `md:` and `lg:` prefixes add desktop enhancements
3. Grid layouts collapse to single column on mobile
4. Navigation converts to hamburger menu on mobile
5. Touch-friendly button sizes (48px minimum)

### Responsive Techniques
- **Flexbox** - Header navigation, card layouts
- **CSS Grid** - Stats cards, gallery grid
- **Hidden/Visible Classes** - `hidden md:flex` for responsive navigation
- **Tailwind Responsive Utilities** - `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`

## 🎨 Design Features

### Color Scheme
- **Primary**: Blue (`blue-500`, `blue-600`)
- **Secondary**: Slate (`slate-800` for header/footer)
- **Success**: Green (`green-500`)
- **Warning**: Yellow (`yellow-100`, `yellow-600`)
- **Danger**: Red (`red-500`)
- **Neutral**: Gray shades

### UX Enhancements
- **Smooth Transitions** - `transition`, `transition-all duration-300`
- **Hover States** - Shadow expansion, color changes, transforms
- **Focus States** - Blue ring (`focus:ring-2 focus:ring-blue-500`)
- **Sticky Header** - `sticky top-0 z-50`
- **Collapsible Modules** - CSS-only collapse with JS toggle
- **Visual Hierarchy** - Font sizes, weights, and spacing

## 🌐 Cross-Browser Compatibility

### Tested Browsers
- ✅ **Chrome** (Latest) - Full support
- ✅ **Firefox** (Latest) - Full support
- ✅ **Safari** (Latest) - Full support
- ✅ **Edge** (Latest) - Full support

### Compatibility Notes
- **Tailwind CSS** - Modern browser support (ES6+)
- **CSS Grid & Flexbox** - Supported in all modern browsers
- **HTML5 Semantic Elements** - Universal support
- **No vendor prefixes needed** - Tailwind handles this

### Testing Recommendations
1. Test on real devices when possible
2. Use browser DevTools responsive mode
3. Check form validation behavior
4. Verify hover/focus states
5. Test navigation menu toggle

## 📂 Project Structure

```
PersonalLearningDashboard/
├── login.html          # Login page
├── dashboard.html      # Main dashboard with modules
├── profile.html        # User profile and settings
├── gallery.html        # Photo gallery
└── README.md           # This file
```

## 🚀 Getting Started

### Installation
No build process required! Simply:
1. Clone or download the project
2. Open any `.html` file in a modern web browser

### Quick Start
```bash
# Navigate to project directory
cd PersonalLearningDashboard

# Open in default browser (example for Windows)
start login.html

# Or serve with a simple HTTP server
python -m http.server 8000
# Then visit http://localhost:8000/login.html
```

## 📝 Implementation Notes

### Why Tailwind CSS?
- **Rapid Development** - Utility classes speed up prototyping
- **Consistency** - Predefined spacing and color system
- **Responsive** - Built-in responsive utilities (`md:`, `lg:`)
- **No Custom CSS** - Minimal additional CSS needed
- **Easy Maintenance** - Changes in HTML, not separate CSS files

### Custom CSS (Minimal)
Only used for:
- Collapsible module animations (`max-height` transitions)
- Toggle button pseudo-elements (`::before`)

### JavaScript (Minimal)
Simple vanilla JS for:
- Module collapse/expand toggle
- Mobile menu toggle
- No frameworks or libraries required

## 🎯 Lab Levels Completed

- ✅ **Level 1**: HTML5 semantic structure
- ✅ **Level 2**: CSS3 fundamentals (replaced with Tailwind)
- ✅ **Level 3**: Tailwind CSS integration
- ✅ **Level 4**: Dashboard with collapsible modules
- ✅ **Level 5**: Responsive design (mobile-first)
- ✅ **Level 6**: Profile module with forms and badges
- ✅ **Level 7**: Gallery with hover effects and grid
- ✅ **Level 8**: Cross-browser support
- ✅ **Level 9**: UX polish (hover, focus, sticky header, transitions)
- ✅ **Level 10**: Documentation and final submission

## 🔮 Future Enhancements

- **Dark Mode** - Toggle between light/dark themes
- **Modal Previews** - Lightbox for gallery images
- **Form Validation** - Client-side validation with error messages
- **Local Storage** - Persist user data
- **Animations** - Entrance animations for cards
- **Search** - Filter modules and topics
- **Backend Integration** - Connect to API for real data

## 📄 License

This project is created for educational purposes as part of the SkillAssure Content Framework.

---

**Built with ❤️ using HTML5, Tailwind CSS, and JavaScript**

*Last Updated: January 1, 2026*
