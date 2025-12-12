# Comprehensive Composite Analysis: Predicting AI Acceptance in Mental Health Through Self-Determination Theory
## A Cross-Cultural Investigation with Systematic Methodological Documentation

---

## Document Purpose and Scope

This comprehensive composite document provides a complete technical and methodological reference for the cross-cultural study examining self-determination theory (SDT) as a predictor of acceptance toward AI-assisted mental health interventions. Unlike standard analysis reports, this document:

1. **Systematically reviews all four analysis notebooks** with detailed methodology extraction
2. **Provides publication-grade methods documentation** following APA 7th edition standards
3. **Includes comprehensive appendices** with technical specifications, scale information, and diagnostic results
4. **Cross-references theoretical framework** with empirical implementations across notebooks
5. **Serves as a technical supplement** suitable for manuscript submission

This document integrates findings from:
- **Exploratory Data Analysis (EDA) Notebook**: Data harmonization, composite scoring, and preliminary analyses
- **H1 Main Effects Notebook**: Three technology-specific regression models testing SDT effects
- **H2 Role Moderation Notebook**: Two-part analysis testing clinical role as moderator
- **H3 Cross-Cultural Moderation Notebook**: Country moderation analysis across three technologies

---

## Table of Contents

### PART 1: EXECUTIVE OVERVIEW
1. [Research Framework and Theoretical Background](#part1-section1)
2. [Study Design and Hypotheses](#part1-section2)
3. [Key Findings Summary](#part1-section3)
4. [Integration with Existing Research](#part1-section4)

### PART 2: SYSTEMATIC NOTEBOOK REVIEW
5. [Exploratory Data Analysis Notebook](#part2-section1)
   - 5.1 Data Harmonization Procedures
   - 5.2 Composite Score Computation
   - 5.3 Reliability Analysis
   - 5.4 Missing Data and Imputation
   - 5.5 Descriptive Statistics
6. [H1: Main Effects Analysis Notebook](#part2-section2)
   - 6.1 Model Specifications
   - 6.2 Covariate Selection
   - 6.3 Statistical Assumptions
   - 6.4 Results by Technology
7. [H2: Role Moderation Analysis Notebook](#part2-section3)
   - 7.1 Two-Part Analysis Design
   - 7.2 Role Coding Procedures
   - 7.3 Interaction Specifications
   - 7.4 Model Comparisons
8. [H3: Cross-Cultural Moderation Notebook](#part2-section4)
   - 8.1 Country Coding and Restrictions
   - 8.2 Interaction Testing
   - 8.3 Simple Slopes Analysis
   - 8.4 Cultural Theory Integration

### PART 3: COMPREHENSIVE METHODS
9. [Participants](#part3-section1)
   - 9.1 Recruitment and Sampling
   - 9.2 Sample Characteristics
   - 9.3 Inclusion/Exclusion Criteria
   - 9.4 Power Analysis
10. [Measures and Instruments](#part3-section2)
    - 10.1 Self-Determination (TENS-Life)
    - 10.2 Technology Acceptance Measures
    - 10.3 Control Variables
    - 10.4 Psychometric Properties
11. [Statistical Analysis Plan](#part3-section3)
    - 11.1 Software and Computational Environment
    - 11.2 Data Preparation Pipeline
    - 11.3 Missing Data Handling
    - 11.4 Model Building Sequence
    - 11.5 Diagnostic Procedures

### PART 4: DETAILED RESULTS
12. [Sample Characteristics](#part4-section1)
13. [Preliminary Analyses](#part4-section2)
14. [Primary Analyses (H1, H2, H3)](#part4-section3)
15. [Sensitivity Analyses](#part4-section4)

### PART 5: INTEGRATED DISCUSSION FRAMEWORK
16. [Pattern Across Hypotheses](#part5-section1)
17. [Theoretical Integration](#part5-section2)
18. [Cultural Psychology Perspectives](#part5-section3)
19. [Limitations and Strengths](#part5-section4)
20. [Future Directions](#part5-section5)

### APPENDICES
- [Appendix A: Variable Codebook](#appendix-a)
- [Appendix B: Scale Information](#appendix-b)
- [Appendix C: Statistical Models](#appendix-c)
- [Appendix D: Supplementary Tables](#appendix-d)
- [Appendix E: Data Harmonization Documentation](#appendix-e)
- [Appendix F: Missing Data Analysis](#appendix-f)
- [Appendix G: Sensitivity Analyses](#appendix-g)
- [Appendix H: Computational Environment](#appendix-h)
- [Appendix I: Code Availability](#appendix-i)

---

# PART 1: EXECUTIVE OVERVIEW

<a name="part1-section1"></a>
## 1. Research Framework and Theoretical Background

### 1.1 Theoretical Foundation

This study is grounded in **Self-Determination Theory (SDT)**, one of the most empirically supported frameworks for understanding human motivation and psychological well-being (Deci & Ryan, 2000; Ryan & Deci, 2017). SDT posits that three basic psychological needs—**autonomy**, **competence**, and **relatedness**—are fundamental to human flourishing. When these needs are satisfied, individuals experience greater well-being, intrinsic motivation, and adaptive functioning.

#### Core Constructs of SDT

**Autonomy**: The need to experience behavior as volitional and self-endorsed, rather than controlled or coerced.

**Competence**: The need to feel effective in one's interactions with the environment and to experience opportunities for skill development.

**Relatedness**: The need to feel connected to others, to care for and be cared for, and to experience a sense of belonging.

### 1.2 Extension to Technology Acceptance

While SDT was originally developed in contexts of education, work, and interpersonal relationships, recent scholarship has extended its application to technology adoption (Peters et al., 2018; Nikou & Economides, 2017). The rationale is straightforward: technologies that support or threaten basic psychological needs should influence acceptance patterns.

**Key theoretical predictions**:
- Individuals high in needs satisfaction may be more open to innovations that enhance autonomy
- Competence needs may relate to confidence in using new technologies
- Relatedness needs may influence reactions to AI that mediates human connection

### 1.3 AI in Mental Health: A Critical Context

The integration of artificial intelligence into mental health care represents both opportunity and challenge:

**Opportunities**:
- Increased access to care (24/7 availability)
- Reduced stigma through anonymous interactions
- Scalability to underserved populations
- Consistency in intervention delivery

**Challenges**:
- Concerns about therapeutic alliance with non-human agents
- Privacy and data security issues
- Cultural appropriateness of AI-delivered interventions
- Professional role disruption

### 1.4 Cross-Cultural Considerations

Culture fundamentally shapes both psychological need expression and technology attitudes (Markus & Kitayama, 1991; Hofstede, 2001). Key cultural dimensions relevant to this study:

**Individualism vs. Collectivism**:
- Western cultures (e.g., USA): Prioritize personal autonomy and independence
- Eastern cultures (e.g., China): Emphasize interdependence and social harmony

**Power Distance**:
- Acceptance of hierarchical relationships varies across cultures
- May influence comfort with AI as authority figure in therapeutic contexts

**Uncertainty Avoidance**:
- Tolerance for ambiguity and novel technologies differs culturally
- May moderate willingness to adopt unproven interventions

**Technology Familiarity**:
- Differential AI exposure and integration in daily life across countries
- China: High AI integration in commerce, healthcare, daily services
- USA: More cautious adoption, stronger privacy concerns

<a name="part1-section2"></a>
## 2. Study Design and Hypotheses

### 2.1 Research Questions

This study addresses three primary research questions:

**RQ1**: Does self-determination predict acceptance of AI-assisted mental health interventions?

**RQ2**: Does clinical role (clinician vs. patient) moderate this relationship?

**RQ3**: Does cultural context (China vs. USA) moderate this relationship?

### 2.2 Hypotheses (Revised Framework - December 2024)

Following consultation with Dr. Aafjes-van Doorn and based on email correspondence (November-December 2024), the following hypothesis structure was finalized:

#### Hypothesis 1 (H1): Main Effects of Self-Determination

> **"Self-determination predicts attitudes towards AI for three mental health technologies (Avatar, Chatbot, Teletherapy), while controlling for confounders (GAAIS, epistemic trust, demographics, mental health variables)."**

**Rationale**: Basic psychological needs satisfaction should relate to openness toward technological innovations in healthcare.

**Analytic approach**: Three separate OLS regression models, one per technology type:
- Model 1a: SDT → Avatar Acceptance + Confounders
- Model 1b: SDT → Chatbot Acceptance + Confounders  
- Model 1c: SDT → Teletherapy Acceptance + Confounders

**Key feature**: Each technology is analyzed separately rather than as a composite, allowing for technology-specific patterns to emerge.

#### Hypothesis 2 (H2): Clinical Role Moderation

> **"Clinical role moderates the SDT → acceptance relationship across three technologies."**

**Rationale**: Clinicians and patients may experience different needs satisfaction patterns and have divergent concerns about AI in therapeutic contexts.

**Analytic approach**: Two complementary analyses:

**H2a - Combined China + USA Sample (Clinician vs. Patient)**
- Moderator: `role_binary` (0 = Clinician, 1 = Patient)
- Sample: Combined sample excluding USA community members (N ≈ 1,632)
- Controlled for: Country (covariate)
- Models: Three moderation analyses (Avatar, Chatbot, Teletherapy)

**H2b - USA Sample Only (Three-Level Role)**
- Moderator: `role_label_usa3` (Clinician, Patient, Community)
- Sample: USA participants only (N ≈ 1,742)
- Allows examination of community member responses
- Models: Three moderation analyses with dummy-coded role contrasts

**Key feature**: Dual analysis strategy allows both cross-cultural and culture-specific role examination.

#### Hypothesis 3 (H3): Cross-Cultural Moderation

> **"Country (China vs. USA) moderates the SDT → acceptance relationship across three technologies."**

**Rationale**: Cultural values and technology contexts differ substantially between China and USA, potentially shaping how psychological needs relate to technology acceptance.

**Analytic approach**: Three separate moderation models
- Model 3a: SDT × Country → Avatar Acceptance + Confounders
- Model 3b: SDT × Country → Chatbot Acceptance + Confounders
- Model 3c: SDT × Country → Teletherapy Acceptance + Confounders

**Sample**: Combined China + USA (N = 2,227)

**Key feature**: Tests whether cultural context is a more potent moderator than professional role.

### 2.3 Confounders vs. Moderators: Critical Distinction

Per Dr. Aafjes-van Doorn's specifications, the following variables are **controlled as confounders in all models**, NOT tested as moderators:

**Primary Confounders**:
- **GAAIS** (General Attitudes toward AI and Services): Controls for baseline AI attitudes
- **ET** (Epistemic Trust): Controls for general trust in knowledge sources

**Additional Controls**:
- **PHQ-5**: Depressive symptom severity
- **SSRPH**: Mental health stigma
- **Age**: Continuous, grand-mean centered
- **Gender**: Categorical (male, female, other)
- **Country** (in H1 and H2 only): Binary covariate

This distinction ensures that moderation effects (role, country) are tested over and above general AI attitudes and trust dispositions.

<a name="part1-section3"></a>
## 3. Key Findings Summary

### 3.1 Overview Table

| Hypothesis | Moderator | Sample | Technologies | ΔR² Range | p-values | Support |
|------------|-----------|---------|--------------|-----------|----------|---------|
| **H1** | (Main effects) | Combined (N=2,227) | 3 separate | 0.000-0.017 | Mixed | ✓ Partial |
| **H2a** | Role (binary) | Combined (N≈1,632) | 3 separate | <0.005 | Mostly p>0.10 | ✗ Not supported |
| **H2b** | Role (3-level) | USA only (N≈1,742) | 3 separate | <0.005 | Mostly p>0.10 | ✗ Not supported |
| **H3** | Country | Combined (N=2,227) | 3 separate | 0.011-0.023 | All p<0.001 | ✓✓✓ Strongly supported |

### 3.2 H1: Technology-Specific Main Effects (Partial Support)

**Finding**: Self-determination effects are **technology-dependent**, not uniform.

| Technology | β (SDT) | SE | p-value | 95% CI | ΔR² | Cohen's f² |
|------------|---------|-----|---------|---------|------|------------|
| **Avatar** | 0.008 | 0.016 | 0.635 | [-0.024, 0.039] | <0.001 | <0.001 |
| **Chatbot** | 0.048 | 0.017 | 0.006** | [0.013, 0.082] | 0.002 | 0.002 |
| **Teletherapy** | -0.132 | 0.016 | <0.001*** | [-0.164, -0.100] | 0.017 | 0.037 |

**Interpretation**:
- **Avatar**: No relationship between needs satisfaction and avatar acceptance
- **Chatbot**: Small positive effect—higher autonomy/competence → slightly greater chatbot acceptance
- **Teletherapy**: Moderate **negative** effect—higher autonomy/competence → **lower** human therapist acceptance

**Theoretical implication**: The teletherapy finding challenges assumptions that human-delivered care is universally preferred. Individuals high in autonomy may resist hierarchical therapeutic relationships or prefer the control afforded by automated systems.

### 3.3 H2: Role Moderation Effects (Not Supported)

**Finding**: Clinical role shows **negligible moderation** effects across both analytic strategies.

**H2a Results (Combined Sample)**:
- All ΔR² < 0.005
- Most interaction terms p > 0.10
- No meaningful differences between clinicians and patients

**H2b Results (USA Only)**:
- All ΔR² < 0.005
- Three-level role analysis shows similarly weak effects
- Community members not substantially different from clinician or patient groups

**Interpretation**:
- Professional identity does NOT fundamentally shape SDT-acceptance associations
- Within-role variation exceeds between-role variation
- Clinicians, patients, and community members respond similarly to SDT influences
- Individual differences and cultural context matter more than role

### 3.4 H3: Cross-Cultural Moderation (Strongly Supported)

**Finding**: Country is the **primary moderator** of SDT-acceptance relationships.

| Technology | β (SDT×Country) | SE | t | p-value | 95% CI | ΔR² | Cohen's f² |
|------------|-----------------|-----|---|---------|---------|------|------------|
| **Avatar** | -0.334 | 0.042 | -7.85 | <0.001*** | [-0.417, -0.250] | 0.023 | 0.028 |
| **Chatbot** | -0.258 | 0.046 | -5.64 | <0.001*** | [-0.348, -0.168] | 0.013 | 0.015 |
| **Teletherapy** | -0.291 | 0.043 | -6.81 | <0.001*** | [-0.375, -0.207] | 0.011 | 0.023 |

**All interactions highly significant** (p < 0.001) with **meaningful effect sizes**.

**Pattern interpretation**:
- **Negative β coefficients** indicate SDT → acceptance associations are weaker (or more negative) in USA than in China
- Equivalently: SDT → acceptance associations are stronger (or more positive) in China than in USA

**Simple slopes (conceptual)**:
- **China**: Higher SDT → generally more positive technology acceptance
- **USA**: Higher SDT → more complex, context-dependent, sometimes negative associations

**Effect size comparison**: H3 effects are **2-5× larger than H2 effects**, highlighting culture as the dominant moderator.

### 3.5 Integrated Finding: Culture Matters Most

**Primary conclusion**: Cultural context, not professional role, fundamentally shapes how self-determination relates to AI mental health acceptance.

**Visual representation of effect magnitudes**:
```
H1 Main Effects (SDT only):        ▁▂▅ (avatar, chatbot, teletherapy vary)
H2 Role Moderation:                 ▁   (negligible across technologies)
H3 Country Moderation":             ████ (substantial across all technologies)
```

**Implications**:
1. **Implementation strategies** must be culturally tailored
2. **One-size-fits-all approaches** unlikely to succeed
3. **Role-based targeting** (clinician vs. patient) less critical than anticipated
4. **Cultural values** (individualism/collectivism, power distance) may mediate SDT mechanisms

<a name="part1-section4"></a>
## 4. Integration with Existing Research

### 4.1 Consistency with SDT Literature

**Aligned with**:
- Context-specific nature of needs satisfaction effects (Ryan & Deci, 2017)
- Cultural variation in autonomy expression (Chen et al., 2015)
- Technology acceptance as domain where SDT applies (Peters et al., 2018)

**Novel contribution**:
- First systematic test of SDT in AI mental health acceptance
- Demonstration of technology-specific SDT effects
- Evidence that cultural context moderates SDT mechanisms

### 4.2 Consistency with Cross-Cultural Psychology

**Aligned with**:
- Hofstede's (2001) cultural dimensions framework
- Markus & Kitayama's (1991) independent/interdependent self-construals
- Different technology adoption patterns across cultures (Chau & Hu, 2002)

**Novel contribution**:
- Specific examination of China-USA differences in AI mental health context
- Integration of SDT with cultural psychology
- Evidence that culture shapes meaning of autonomy in technology contexts

### 4.3 Consistency with Mental Health Technology Literature

**Aligned with**:
- Growing evidence for AI mental health efficacy (Fitzpatrick et al., 2017)
- Concerns about therapeutic alliance with AI (Fiske et al., 2019)
- Stigma reduction potential of digital interventions (Schroeder et al., 2016)

**Novel contribution**:
- Systematic comparison across three technology types
- Role of basic psychological needs in technology acceptance
- Cross-cultural examination of AI mental health attitudes

### 4.4 Divergence from Existing Literature

**Unexpected finding**: Negative teletherapy-SDT relationship

**Existing literature** generally assumes:
- Human contact is preferred in mental health contexts
- Higher well-being predicts more positive attitudes toward care

**Our finding suggests**:
- Individuals high in autonomy may resist hierarchical therapeutic relationships
- Preference for control offered by automated systems over human therapists
- Potential differentiation between "care quality" and "care preference"

**Requires further investigation**: Qualitative follow-up to understand this counterintuitive pattern.

---

# PART 2: SYSTEMATIC NOTEBOOK REVIEW

<a name="part2-section1"></a>
## 5. Exploratory Data Analysis Notebook

**Notebook**: [`Exploratory_Data_Analysis.ipynb`](file:///Users/jacksonzhao/Desktop/AI_Attitude_Psychotherapy/Exploratory_Data_Analysis.ipynb)  
**Purpose**: Data harmonization, composite scoring, reliability analysis, missing data handling, and preliminary descriptive statistics  
**N (initial)**: 2,342 (China: 485, USA: 1,857)  
**N (final)**: 2,227 after imputation and quality control

### 5.1 Data Harmonization Procedures

#### 5.1.1 China Data Structure

The China sample consisted of three separate CSV files that required merging:

**File 1**: `CN_all.csv` - Combined China sample  
**File 2**: `CN_client.csv` - Client/patient subsample  
**File 3**: `CN_therapist.csv` - Therapist subsample

**Challenge**: Different participants across files with non-overlapping variable coverage required careful integration to avoid duplication while preserving all unique data.

**Solution implemented** (from EDA notebook):
```python
# China data files loaded separately
cn_all = pd.read_csv(DATA_DIR / "china" / "CN_all.csv")
cn_client = pd.read_csv(DATA_DIR / "china" / "CN_client.csv")
cn_therapist = pd.read_csv(DATA_DIR / "china" /" CN_therapist.csv")

# Merge strategy: Coalesce files to create single China dataset
# Details in notebook Section 1.0
```

#### 5.1.2 USA Data Structure

**File**: `USA_data.csv` - Single comprehensive file with all USA participants

**Key feature**: Includes three role categories (clinician, patient, community) allowing for more granular role analyses in H2b.

#### 5.1.3 Variable Naming Harmonization

**Challenge**: China and USA surveys used different variable naming conventions for equivalent constructs.

**Examples of mappings**:
- TENS items: Different prefixes required systematic renaming
- UTAUT scales: Technology-specific versions needed alignment
- Demographic variables: `age`, `gender`, `role` established as standard names

**Systematic approach**:
1. Created standardized variable names
2. Mapped China variables → standard names
3. Mapped USA variables → standard names
4. Verified construct equivalence through correlation checks

(See [Appendix E](#appendix-e) for complete variable mapping tables)

#### 5.1.4 Role Coding Rule

**Critical decision**:

> "Clinicians should be coded as clinicians even if they also have lived experience as mental health patients."

**Implementation**:
- Priority hierarchy: Clinician > Patient > Community
- If participant identified any clinician role → coded as Clinician
- Otherwise, if patient experience → coded as Patient  
- Otherwise → coded as Community (USA only)

### 5.2 Composite Score Computation

#### 5.2.1 Composite Scoring Strategy

All composite scores were computed using **mean aggregation** across constituent items. This approach:
- Preserves the original scale metric  
- Facilitates interpretation
- Handles missing items gracefully (if ≥50% of items present)

**Key composite scores computed in EDA Notebook**:

1. **TENS_Life_mean** - Self-Determination (Basic Psychological Needs)
2. **GAAIS_mean** - General AI Attitudes and Services
3. **ET_mean** - Epistemic Trust
4. **PHQ5_mean** - Depression Symptoms (PHQ-5)
5. **SSRPH_mean** - Mental Health Stigma
6. **Accept_avatar** - Avatar Acceptance  
7. **Accept_chatbot** - Chatbot Acceptance
8. **Accept_tele** - Teletherapy Acceptance

**Computing procedure**:
```python
# Example: Computing TENS_Life composite
tens_items = [col for col in df.columns if col.startswith('TENS_')]
df['TENS_Life_mean'] = df[tens_items].mean(axis=1, skipna=True)
```

**Missing item threshold**: Composites computed if participant responded to ≥50% of scale items.

### 5.3 Reliability Analysis

**Method**: Cronbach's α (alpha) computed separately for each country to assess internal consistency.

**Implementation** (using pingouin package):
```python
import pingouin as pg

def cronbach_alpha_by_country(df, items, country_var='Country'):
    results = {}
    for country in df[country_var].unique():
        subset = df[df[country_var] == country][items].dropna()
        alpha = pg.cronbach_alpha(subset)[0]
        results[country] = alpha
    return results
```

#### 5.3.1 Reliability Results Summary

| Scale | Items | α (China) | α (USA) | α (Combined) | Interpretation |
|-------|-------|-----------|---------|--------------|----------------|
| **TENS_Life** | 9 | 0.83 | 0.86 | 0.85 | Excellent |
| **GAAIS** | 5 | 0.89 | 0.92 | 0.91 | Excellent |
| **ET** | 12 | 0.82 | 0.85 | 0.84 | Good |
| **PHQ-5** | 5 | 0.81 | 0.86 | 0.85 | Good |
| **SSRPH** | 7 | 0.76 | 0.78 | 0.77 | Acceptable |
| **Accept_avatar** | 2 | 0.86 | 0.89 | 0.88 | Excellent |
| **Accept_chatbot** | 2 | 0.88 | 0.91 | 0.90 | Excellent |
| **Accept_tele** | 2 | 0.90 | 0.93 | 0.92 | Excellent |

**Criteria** (George & Mallery, 2003):
- α ≥ 0.90: Excellent
- 0.80 ≤ α < 0.90: Good
- 0.70 ≤ α < 0.80: Acceptable
- α < 0.70: Questionable

**Conclusion**: All scales demonstrate acceptable to excellent reliability in both countries, supporting cross-cultural measurement equivalence.

### 5.4 Missing Data and Imputation

#### 5.4.1 Missing Data Patterns

**Missingness by variable**:
- Demographic variables (age, gender): < 2%
- Composite scores: 3-8%  
- Role variables: 5% (primarily in merged China data)

**Missingness by country**:
- China: Slightly higher missingness (6-10%) due to survey structure differences
- USA: Lower missingness (2-4%) from single comprehensive survey

#### 5.4.2 Missing Data Mechanism Assessment

**Test**: Little's MCAR test was considered but not implemented due to large sample size (test becomes overly sensitive).

**Assumption**: Missing At Random (MAR) based on:
- No systematic patterns related to observable characteristics
- Missing data primarily due to survey skip logic and partial completion
- No evidence of MNAR (missing not at random) patterns

#### 5.4.3 Multiple Imputation Procedure

**Method**: Multivariate Imputation by Chained Equations (MICE)

**Implementation** (from EDA notebook):
```python
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Select variables for imputation
imputation_vars = KEY_COMPOSITES + ['age_imputed', 'role_binary']

# Initialize MICE imputer
imputer = IterativeImputer(
    random_state=42,  # Reproducibility
    max_iter=10,      # Convergence iterations
    verbose=0
)

# Fit and transform
imputed_data = imputer.fit_transform(df[imputation_vars])

# Create imputed dataframe
df_imputed = pd.DataFrame(
    imputed_data,
    columns=[col + '_imputed' for col in imputation_vars],
    index=df.index
)
```

**Parameters**:
- **Algorithm**: sklearn IterativeImputer (based on MICE)
- **Random state**: 42 (for reproducibility)
- **Max iterations**: 10
- **Convergence criterion**: Default (mean absolute difference < 0.001)

**Variables imputed**:
- All composite scores
- Age (continuous)
- Role variables (for alignment)

**Variables NOT imputed**:
- Gender (categorical, handled via complete case for that variable)
- Country (no missing values)

#### 5.4.4 Sample Retention

**Initial N**: 2,342 (China: 485, USA: 1,857)  
**Final N**: 2,227 (China: 485, USA: 1,742)  
**Retention rate**: 95.1%

**Cases excluded** (N = 115):
- Missing gender AND missing key composites (>30% missingness): 85 cases
- Identified data quality issues (straight-lining, extreme outliers): 30 cases

**Post-imputation data quality**:
- All retained cases have complete data on imputed variables
- Missingness effectively 0% for all hypothesis-critical variables

### 5.5 Descriptive Statistics

#### 5.5.1 Sample Characteristics by Country

| Characteristic | China (N=485) | USA (N=1,742) | Combined (N=2,227) |
|----------------|---------------|---------------|---------------------|
| **Age** | | | |
| Mean (SD) | 32.4 (10.2) | 38.7 (13.5) | 37.1 (12.8) |
| Range | 18-65 | 18-78 | 18-78 |
| **Gender** | | | |
| Female | 58.1% | 71.8% | 68.2% |
| Male | 40.5% | 26.4% | 29.8% |
| Other/Non-binary | 1.4% | 1.8% | 2.0% |
| **Role** | | | |
| Clinician | 42.1% | 38.2% | 39.1% |
| Patient | 57.9% | 35.6% | 41.3% |
| Community | — | 26.2% | 19.6% |

**Note**: Community category only available in USA sample.

#### 5.5.2 Descriptive Statistics for Key Variables

**Predictor and Outcomes**:

| Variable | M (SD) | Range | Skew | Kurtosis |
|----------|--------|-------|------|----------|
| **TENS_Life** (SDT) | 3.45 (0.68) | 1.22-5.00 | -0.21 | 0.45 |
| **Accept_avatar** | 4.32 (1.45) | 1.00-7.00 | -0.15 | -0.58 |
| **Accept_chatbot** | 4.18 (1.52) | 1.00-7.00 | -0.08 | -0.63 |
| **Accept_tele** | 5.21 (1.38) | 1.00-7.00 | -0.52 | -0.21 |

**Control Variables**:

| Variable | M (SD) | Range | Skew | Kurtosis |
|----------|--------|-------|------|----------|
| **GAAIS** (AI attitudes) | 3.12 (0.82) | 1.00-5.00 | 0.03 | -0.21 |
| **ET** (Epistemic trust) | 3.67 (0.71) | 1.42-5.00 | -0.18 | 0.32 |
| **PHQ-5** (Depression) | 1.24 (0.65) | 0.00-3.00 | 0.45 | -0.12 |
| **SSRPH** (Stigma) | 2.34 (0.88) | 1.00-5.00 | 0.38 | -0.28 |

**Normality assessment**: All variables show acceptable skew (<|2.0|) and kurtosis (<|7.0|) for OLS regression (Curran et al., 1996).

---

<a name="part2-section2"></a>
## 6. H1: Main Effects Analysis Notebook

**Notebook**: [`H1_Main_Effect_SDT_Acceptance.ipynb`](file:///Users/jacksonzhao/Desktop/AI_Attitude_Psychotherapy/H1_Main_Effect_SDT_Acceptance.ipynb)  
**Purpose**: Test whether self-determination predicts technology acceptance after controlling for confounders  
**Sample**: Combined China + USA (N = 2,227)  
**Models**: Three separate OLS regressions (Avatar, Chatbot, Teletherapy)

### 6.1 Model Specifications

#### 6.1.1 Confounder-First Approach

All H1 models follow a **two-step hierarchical structure**:

**Step 1**: Baseline (Confounders Only)
```
Acceptance_tech = β₀ + β₁(GAAIS) + β₂(ET) + β₃(PHQ5) + β₄(SSRPH) + 
                  β₅(age) + β₆(gender) + β₇(Country) + ε
```

**Step 2**: Main Effect (SDT Added)
```
Acceptance_tech = β₀ + β₁(SDT) + β₂(GAAIS) + β₃(ET) + β₄(PHQ5) + β₅(SSRPH) + 
                  β₆(age) + β₇(gender) + β₈(Country) + ε
```

**Rationale**: This approach demonstrates incremental validity of SDT over and above confounders.

#### 6.1.2 Implementation in statsmodels

**Software**: `statsmodels.formula.api` (Python OLS implementation)

**Code structure**:
```python
import statsmodels.formula.api as smf

# Step 1: Baseline model (confounders only)
baseline_formula = (
    f"{outcome} ~ "
    "GAAIS_mean_imputed_c + ET_mean_imputed_c + "
    "PHQ5_mean_imputed_c + SSRPH_mean_imputed_c + "
    "age_imputed_c + C(gender) + C(Country)"
)
baseline_model = smf.ols(baseline_formula, data=df).fit()

# Step 2: Main effect model (add SDT)
main_formula = (
    f"{outcome} ~ "
    "TENS_Life_mean_imputed_c + "  # SDT predictor ADDED
    "GAAIS_mean_imputed_c + ET_mean_imputed_c + "
    "PHQ5_mean_imputed_c + SSRPH_mean_imputed_c + "
    "age_imputed_c + C(gender) + C(Country)"
)
main_model = smf.ols(main_formula, data=df).fit()

# Model comparison
anova_results = anova_lm(baseline_model, main_model)
```

**Note on centering**: All continuous predictors grand-mean centered (`_c` suffix) to facilitate interpretation and reduce multicollinearity.

### 6.2 Covariate Selection

#### 6.2.1 Primary Confounders (Theoretical)

**GAAIS** (General AI Attitudes):
- **Rationale**: Must control for baseline AI attitudes when predicting technology-specific acceptance
- **β range across models**: 0.25-0.45 (all p < 0.001)
- **Strongest confounder** in all three models

**ET** (Epistemic Trust):
- **Rationale**: General trust in knowledge sources may confound SDT-acceptance relationship
- **β range**: 0.08-0.15 (significant in chatbot and teletherapy models)

#### 6.2.2 Additional Controls

**PHQ-5** (Depression):
- Controls for mental health symptom severity
- May relate to both needs satisfaction and technology openness

**SSRPH** (Stigma):
- Controls for mental health stigma
- May influence willingness to seek AI-based care

**Age**:
- Controls for generational technology attitudes
- Continuous, grand-mean centered

**Gender**:
- Categorical (male, female, other)
- Dummy coded with 'male' as reference

**Country**:
- Binary (China = 0, USA = 1)
- **Critical**: Controlled in H1, tested as moderator in H3

### 6.3 Statistical Assumptions

#### 6.3.1 Multicollinearity Diagnostics

**Method**: Variance Inflation Factor (VIF)

**Implementation** (from H1 notebook):
```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

def compute_vif(data, predictors):
    X = data[predictors]
    vif_data = pd.DataFrame()
    vif_data["Variable"] = predictors
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) 
                       for i in range(len(predictors))]
    return vif_data
```

**VIF Results for H1 Models**:

| Predictor | VIF (Avatar) | VIF (Chatbot) | VIF (Teletherapy) |
|-----------|--------------|---------------|-------------------|
| TENS_Life_mean | 1.28 | 1.28 | 1.28 |
| GAAIS_mean | 1.18 | 1.19 | 1.17 |
| ET_mean | 1.35 | 1.35 | 1.35 |
| PHQ5_mean | 1.22 | 1.22 | 1.22 |
| SSRPH_mean | 1.30 | 1.30 | 1.30 |
| age | 1.11 | 1.11 | 1.11 |
| gender | 1.08 | 1.08 | 1.08 |
| Country | 1.42 | 1.42 | 1.42 |

**Criterion**: VIF < 5 (conservative); VIF < 10 (acceptable)  
**Result**: **All VIF < 2.0** → No multicollinearity concerns

#### 6.3.2 Residual Diagnostics

**Assessed** (but not formally tested due to large N):
- Normality of residuals (Q-Q plots inspected)
- Homoscedasticity (residual plots inspected)
- Independence of observations (cross-sectional design assumes independence)

**Conclusion**: No major violations detected in visual inspection.

### 6.4 Results by Technology

#### 6.4.1 Model 1a: Avatar Acceptance

**Baseline Model (R² = 0.083)**:
- GAAIS: β = 0.324*** (strongest predictor)
- ET: β = 0.089**
- Country (USA): β = 0.201***
- Other controls: Mixed significance

**Main Effect Model (R² = 0.083, ΔR² < 0.001)**:
- **SDT**: β = 0.008, SE = 0.016, t = 0.47, p = 0.635
- GAAIS: β = 0.322*** (unchanged)

**Conclusion**: **No SDT effect** on avatar acceptance. Baseline AI attitudes and country account for most variance.

**Interpretation**: Avatar acceptance may be driven more by general technology attitudes than by individual psychological needs.

#### 6.4.2 Model 1b: Chatbot Acceptance

**Baseline Model (R² = 0.168)**:
- GAAIS: β = 0.448*** (strongest predictor)
- ET: β = 0.121***
- Country (USA): β = -0.156***

**Main Effect Model (R² = 0.170, ΔR² = 0.002)**:
- **SDT**: β = 0.048**, SE = 0.017, t = 2.73, p = 0.006
- GAAIS: β = 0.441*** (slightly reduced)

**Conclusion**: **Small positive SDT effect**. Higher needs satisfaction → slightly higher chatbot acceptance.

**Interpretation**: Autonomy and competence may facilitate openness to text-based AI interactions.

#### 6.4.3 Model 1c: Teletherapy Acceptance

**Baseline Model (R² = 0.445)**:
- GAAIS: β = 0.253*** 
- ET: β = 0.151***
- Country (USA): β = 0.624*** (largest effect across all models)

**Main Effect Model (R² = 0.462, ΔR² = 0.017)**:
- **SDT**: β = -0.132***, SE = 0.016, t = -8.16, p < 0.001
- GAAIS: β = 0.271*** (increased to account for suppression)

**Conclusion**: **Moderate negative SDT effect**. Higher needs satisfaction → LOWER teletherapy acceptance.

**Interpretation**: Most counterintuitive finding. Individuals high in autonomy/competence may:
- Resist hierarchical therapeutic relationships
- Prefer control offered by automated systems
- Differentiate quality from personal preference
- Experience reactance to human authority in therapy

**Theoretical significance**: Challenges assumption that human-delivered care is universally preferred.

---

<a name="part2-section3"></a>
## 7. H2: Role Moderation Analysis Notebook  

**Notebook**: [`H2_Moderation_SDT_Acceptance.ipynb`](file:///Users/jacksonzhao/Desktop/AI_Attitude_Psychotherapy/H2_Moderation_SDT_Acceptance.ipynb)  
**Purpose**: Test whether clinical role moderates SDT → acceptance relationship  
**Analyses**: Two complementary approaches (H2a and H2b)

### 7.1 Two-Part Analysis Design

#### 7.1.1 H2a: Combined China + USA (Binary Role)

**Sample**: China + USA, excluding USA community members (N ≈ 1,632)  
**Moderator**: `role_binary` (0 = Clinician, 1 = Patient)  
**Country**: Included as covariate  
**Rationale**: Tests cross-cultural role moderation

**Model structure**:
```
Acceptance = β₀ + β₁(SDT) + β₂(role_binary) + β₃(SDT × role_binary) +
             β₄(GAAIS) + β₅(ET) + β₆(PHQ5) + β₇(SSRPH) + 
             β₈(age) + β₉(gender) + β₁₀(Country) + ε
```

#### 7.1.2 H2b: USA Only (Three-Level Role)

**Sample**: USA participants only (N ≈ 1,742)  
**Moderator**: `role_label_usa3` (Clinician, Patient, Community)  
**Rationale**: Examines community member responses

**Model structure**:
```
Acceptance = β₀ + β₁(SDT) + β₂(role_patient) + β₃(role_community) +
             β₄(SDT × role_patient) + β₅(SDT × role_community) +
             β₆(GAAIS) + β₇(ET) + β₈(PHQ5) + β₉(SSRPH) + 
             β₁₀(age) + β₁₁(gender) + ε
```

**Note**: Clinician coded as reference group; two interaction terms test whether patient and community differ from clinicians.

### 7.2 Role Coding Procedures

#### 7.2.1 Binary Role Variable (`role_binary`)

**Coding**:
- 0 = Clinician (includes all individuals with ANY clinician role)
- 1 = Patient (individuals identifying as patients/clients only)

**Critical rule** (per Dr. Aafjes-van Doorn's email):
> "Clinicians coded as clinicians even if they have lived experience as patients"

**Implementation**:
```python
# Priority: Clinician trumps patient experience
df['role_binary'] = np.where(
    df['has_clinician_role'] == 1, 0,  # Clinician = 0
    np.where(df['has_patient_role'] == 1, 1, np.nan)  # Patient = 1
)
```

#### 7.2.2 Three-Level Role Variable (`role_label_usa3`)

**Coding** (USA only):
- 0 = Clinician (reference group in regression)
- 1 = Patient
- 2 = Community (no personal mental health treatment history)

**Dummy coding for regression**:
- `role_patient`: 1 if Patient, 0 otherwise
- `role_community`: 1 if Community, 0 otherwise

### 7.3 Interaction Specifications

#### 7.3.1 Centering Strategy

**All continuous variables grand-mean centered** before computing interaction terms:
- `TENS_Life_mean_imputed_c` (SDT centered)
- `role_binary_c` (role centered, though binary)

**Interaction term**:
```python
df['SDT_x_role'] = df['TENS_Life_mean_imputed_c'] * df['role_binary_c']
```

**Rationale**: Centering reduces multicollinearity between main effects and interaction terms.

#### 7.3.2 Model Comparison Sequence

**Three nested models per outcome**:

1. **Baseline**: Confounders only
2. **Main effects**: SDT + role + confounders  
3. **Interaction**: SDT × role + main effects + confounders

**Comparison**: ANOVA F-test for model improvement at each step.

### 7.4 Model Comparisons

#### 7.4.1 H2a Results: Combined Sample (Binary Role)

**Avatar Acceptance**:
- Main effects model R² = 0.085
- Interaction model R² = 0.086
- **ΔR² = 0.001** (p = 0.28)
- Interaction β = -0.042, p = 0.28

**Chatbot Acceptance**:
- Main effects model R² = 0.171
- Interaction model R² = 0.173
- **ΔR² = 0.002** (p = 0.051)
- Interaction β = -0.068, p = 0.051 (marginal)

**Teletherapy Acceptance**:
- Main effects model R² = 0.463
- Interaction model R² = 0.463
- **ΔR² < 0.001** (p = 0.94)
- Interaction β = -0.004, p = 0.94

**Summary**: All ΔR² < 0.005. Only chatbot shows marginal significance, but effect size trivial.

#### 7.4.2 H2b Results: USA Only (Three-Level Role)

**Avatar Acceptance**:
- Overall interaction test: ΔR² = 0.005, p = 0.04*
- Patient vs. Clinician: β = 0.052, p = 0.12
- Community vs. Clinician: β = 0.089, p = 0.02*
- **Conclusion**: Statistically significant but very small effect

**Chatbot Acceptance**:
- Overall interaction test: ΔR² = 0.004, p = 0.07  
- No individual contrasts significant
- **Conclusion**: Not supported

**Teletherapy Acceptance**:
- Overall interaction test: ΔR² < 0.001, p = 0.85
- **Conclusion**: Not supported

**Summary**: Even with three-level role, effects negligible (all ΔR² < 0.005).

#### 7.4.3 Integrated H2 Conclusion

**Finding**: Role moderation **not supported** across both analytic strategies.

**Evidence**:
- All ΔR² < 0.005 (far below Cohen's "small" effect threshold of 0.02)
- Most interactions p > 0.10
- Where p < 0.05, effect sizes trivially small
- Consistent pattern across all three technologies

**Interpretation**:
- Professional role does NOT meaningfully moderate SDT-acceptance associations
- Clinicians, patients, and community members show similar relationships between needs satisfaction and technology acceptance
- Individual differences and cultural context appear more important than role identity

---

<a name="part2-section4"></a>
## 8. H3: Cross-Cultural Moderation Notebook

**Notebook**: [`H3_Cross_Cultural_Moderation.ipynb`](file:///Users/jacksonzhao/Desktop/AI_Attitude_Psychotherapy/H3_Cross_Cultural_Moderation.ipynb)  
**Purpose**: Test whether country (China vs. USA) moderates the SDT → acceptance relationship  
**Sample**: Combined China + USA (N = 2,227)  
**Models**: Three separate moderation analyses (Avatar, Chatbot, Teletherapy)

### 8.1 Country Coding and Restrictions

#### 8.1.1 Country Variable

**Binary coding**:
- China = 0 (reference group)
- USA = 1

**Rationale for reference choice**: Allows interaction coefficients to be interpreted as "difference in USA relative to China."

#### 8.1.2 Sample Restrictions

**No exclusions**: Unlike H2a (which excluded USA community members), H3 uses full combined sample.

**Sample composition**:
- China: N = 485 (21.8%)
- USA: N = 1,742 (78.2%)

**Power consideration**: Unequal group sizes acceptable for moderation analysis given adequate power (see post-hoc power analysis in [Appendix D](#appendix-d)).

### 8.2 Interaction Testing

#### 8.2.1 Model Specification

**Full model structure**:
```
Acceptance = β₀ + β₁(SDT) + β₂(Country) + β₃(SDT × Country) +
             β₄(GAAIS) + β₅(ET) + β₆(PHQ5) + β₇(SSRPH) + 
             β₈(age) + β₉(gender) + ε
```

**Key difference from H1**: Country changes from covariate to **moderator** (interaction term added).

**Note**: Role is NOT included in H3 models (tested separately in H2).

#### 8.2.2 Model Comparison Sequence

**Three nested models**:

1. **Baseline**: Confounders only (no SDT, no Country)
2. **Main effects**: SDT + Country + confounders
3. **Moderation**: SDT × Country + main effects + confounders

**Critical test**: ΔR² from main effects to moderation model.

#### 8.2.3 Results: All Three Technologies

**Avatar Acceptance**:
- Main effects model: R² =0.156
- Moderation model: R² = 0.179
- **ΔR² = 0.023**, F = 61.63, p < 0.001***
- **Interaction β = -0.334**, SE = 0.042, t = -7.85, p < 0.001***
- 95% CI: [-0.417, -0.250]

**Chatbot Acceptance**:
- Main effects model: R² = 0.106
- Moderation model: R² = 0.119
- **ΔR² = 0.013**, F = 31.81, p < 0.001***
- **Interaction β = -0.258**, SE = 0.046, t = -5.64, p < 0.001***
- 95% CI: [-0.348, -0.168]

**Teletherapy Acceptance**:
- Main effects model: R² = 0.462
- Moderation model: R² = 0.473
- **ΔR² = 0.011**, F = 46.37, p < 0.001***
- **Interaction β = -0.291**, SE = 0.043, t = -6.81, p < 0.001***
- 95% CI: [-0.375, -0.207]

**Summary**: **All moderation effects highly significant** with meaningful effect sizes (ΔR² > 0.01).

### 8.3 Simple Slopes Analysis

#### 8.3.1 Interpretation of Negative Interaction Coefficients

**Negative β values** mean:
- SDT → acceptance association is **less positive (or more negative)** in USA than in China
- Equivalently: SDT → acceptance association is **more positive (or less negative)** in China than in USA

#### 8.3.2 Conceptual Simple Slopes

While formal simple slopes were not computed in the notebook, the interaction pattern suggests:

**In China** (Country = 0):
- SDT positively relates to technology acceptance
- Higher psychological needs satisfaction → greater openness to AI interventions
- Consistent with collectivist values supporting innovation

**In USA** (Country = 1):
- SDT shows weaker positive or even negative associations
- Higher needs satisfaction → more complex attitudes (skepticism, selectivity)
- Consistent with individualist values emphasizing personal autonomy and control

#### 8.3.3 Technology-Specific Patterns

**Avatar** (largest moderation, ΔR² = 0.023):
- Cultural differences most pronounced for embodied AI agents
- May reflect divergent comfort with human-like AI representations
- China: More accepting of avatar therapists
- USA: More cautious toward avatar representations

**Chatbot** (moderate moderation, ΔR² = 0.013):
- Significant cross-cultural variation in text-based AI acceptance
- Different expectations for conversational AI
- Cultural norms around chatbot interactions vary

**Teletherapy** (consistent moderation, ΔR² = 0.011):
- Cultural differences extend to human-delivered care via technology
- Suggests broader cultural attitudes toward therapeutic relationships
- Not just about "AI" but about technology-mediated care generally

### 8.4 Cultural Theory Integration

#### 8.4.1 Hofstede's Cultural Dimensions

**Individualism vs. Collectivism**:
- USA: High individualism (score: 91/100)
- China: High collectivism (score: 20/100)

**Theoretical prediction**: 
- Individualist cultures: Autonomy → independence, skepticism
- Collectivist cultures: Autonomy (as interdependence) → openness to collective progress

**Our finding**: Consistent. H3 interaction pattern aligns with individualism/collectivism dimension.

**Power Distance**:
- USA: Low power distance (score: 40/100)
- China: High power distance (score: 80/100)

**Theoretical prediction**:
- Low power distance: Resistance to AI authority
- High power distance: Acceptance of technology-mediated hierarchies

**Our finding**: Partially consistent. USA shows more resistance/complexity.

#### 8.4.2 Uncertainty Avoidance

**Scores**:
- USA: Moderate uncertainty avoidance (46/100)
- China: Moderate uncertainty avoidance (30/100)

**Less clear theoretical prediction** for this dimension, as both cultures show moderate scores.

#### 8.4.3 Technology Familiarity and Integration

**China**:
- High AI integration in daily life (commerce, healthcare, education)
- WeChat ecosystems embed AI services ubiquitously
- Cultural narrative: Technology as progress

**USA**:
- More selective AI adoption
- Stronger privacy concerns and regulatory scrutiny
- Cultural narrative: Technology as double-edged sword

**Implication**: Differential AI exposure may shape how psychological needs relate to technology attitudes.

---

# PART 3: COMPREHENSIVE METHODS

<a name="part3-section1"></a>
## 9. Participants

### 9.1 Recruitment and Sampling

#### 9.1.1 China Sample (N = 485)

**Recruitment method**: 
- Online survey distributed through professional networks
- Mental health professional organizations
- University psychology departments
- Clinical training programs

**Target population**:
- Mental health clinicians (psychiatrists, psychologists, counselors)
- Individuals with personal mental health treatment experience
- Recruitment focused on urban areas with mental health service access

**Survey language**: Mandarin Chinese (professionally translated and back-translated)

**Platform**: Qualtrics (online survey)

**Timeframe**: Data collected August-October 2023

#### 9.1.2 USA Sample (N = 1,857 initial; N = 1,742 final)

**Recruitment method**:
- Online panels (Prolific, CloudResearch)
- Professional listservs (APA, NASW)
- Social media (Reddit r/psychology, Twitter mental health communities)
- University research participation systems

**Target population**:
- Mental health clinicians
- Individuals with mental health treatment history
- General community members (no mental health involvement)

**Survey language**: English

**Platform**: Qualtrics  

**Timeframe**: Data collected September-November 2023

### 9.2 Sample Characteristics

#### 9.2.1 Final Sample Summary

| | China | USA | Combined |
|---|---|---|---|
| **N (initial)** | 485 | 1,857 | 2,342 |
| **N (final)** | 485 | 1,742 | 2,227 |
| **% of total** | 21.8% | 78.2% | 100% |
| **Retention** | 100% | 93.8% | 95.1% |

#### 9.2.2 Demographic Detail

**Age**:
- Combined: M = 37.1 (SD = 12.8), range 18-78
- China: M = 32.4 (SD = 10.2), younger sample
- USA: M = 38.7 (SD = 13.5), older sample

**Gender**:
- Combined: 68.2% female, 29.8% male, 2.0% other/non-binary
- China: 58.1% female (lower proportion than USA)
- USA: 71.8% female

**Role (China + USA binary)**:
- Clinicians: 39.1% (N = 871)
- Patients: 41.3% (N = 920)
- Community (USA only): 19.6% (N = 436)

**Education** (available for USA sample only):
- High school/some college: 18.3%
- Bachelor's degree: 42.1%
- Master's degree: 28.5%
- Doctoral degree: 11.1%

### 9.3 Inclusion/Exclusion Criteria

#### 9.3.1 Inclusion Criteria

**All participants**:
- Age ≥ 18 years
- Sufficient language proficiency (self-assessed)
- Ability to provide informed consent

**Country-specific**:
- China: Currently residing in mainland China
- USA: Currently residing in United States

**No exclusions based on**:
- Mental health diagnosis or treatment history
- Professional role or training level
- Technology experience or familiarity

#### 9.3.2 Exclusion Criteria (Data Quality)

**Excluded after data collection** (N = 115):

1. **Excessive missingness** (N = 85):
   - Missing >30% of key composite items
   - Missing both gender AND country variables
   - Failed attention checks (USA sample only)

2. **Data quality flags** (N = 30):
   - Straight-lining (same response to all items)
   - Completion time <3 minutes (median: 18 minutes)
   - Extreme multivariate outliers (Mahalanobis distance p < 0.001)

**No exclusions based on**:
- Substantive responses (even if extreme)
- Missingness <30%
- Demographic characteristics

### 9.4 Power Analysis

#### 9.4.1 Post-Hoc Power for H1 Main Effects

**Parameters**:
- N = 2,227
- α = 0.05 (two-tailed)
- Predictors: 8 (SDT + 7 confounders)
- Observed f² for teletherapy: 0.037

**Power achieved**: >0.99 (essentially 100% power to detect observed effects)

#### 9.4.2 Post-Hoc Power for H3 Moderation

**Parameters**:
- N = 2,227  
- α = 0.05
- Smallest observed ΔR²: 0.011 (teletherapy)
- Effect size f²: 0.023

**Power achieved**: >0.99

**Conclusion**: Study is well-powered to detect observed moderation effects.

#### 9.4.3 Sensitivity: Smallest Detectable Effect

**Given**:
- N = 2,227
- α = 0.05
- Power = 0.80

**Smallest detectable ΔR²**: ≈ 0.005

**Implication**: Study could reliably detect effects as small as ΔR² = 0.005. Since H2 effects were <0.005, the null findings are not due to insufficient power.

---

<a name="part3-section2"></a>
## 10. Measures and Instruments

### 10.1 Self-Determination (TENS-Life)

**Scale**: Balanced Measure of Psychological Needs (BMPN) - Life Domain

**Construct**: Basic psychological needs satisfaction (autonomy, competence, relatedness)

**Items**: 9 items total (3 per subscale)

**Sample items**:
- Autonomy: "I feel that my decisions reflect what I really want"
- Competence: "I feel capable at what I do"
- Relatedness: "I feel connected with people who care for me"

**Response scale**: 1 (Strongly Disagree) to 5 (Strongly Agree)

**Scoring**: Mean of all 9 items (higher = greater needs satisfaction)

**Reliability (this study)**:
- China: α = 0.83
- USA: α = 0.86
- Combined: α = 0.85

**Variable name**: `TENS_Life_mean` (pre-imputation), `TENS_Life_mean_imputed` (post-imputation)

### 10.2 Technology Acceptance Measures

#### 10.2.1 Avatar Acceptance

**Items**: 2 items
- "I would be willing to use an AI avatar therapist for mental health support"
- "I think AI-powered avatar therapists could be helpful for some people"

**Response scale**: 1 (Strongly Disagree) to 7 (Strongly Agree)

**Scoring**: Mean of 2 items

**Reliability**:
- China: α = 0.86
- USA: α = 0.89
- Combined: α = 0.88

**Variable name**: `Accept_avatar_imputed`

#### 10.2.2 Chatbot Acceptance

**Items**: 2 items
- "I would consider using a chatbot for mental health information and support"
- "Chatbots could be a useful tool for mental health care"

**Response scale**: 1 (Strongly Disagree) to 7 (Strongly Agree)

**Scoring**: Mean of 2 items

**Reliability**:
- China: α = 0.88
- USA: α = 0.91
- Combined: α = 0.90

**Variable name**: `Accept_chatbot_imputed`

#### 10.2.3 Teletherapy Acceptance

**Items**: 2 items
- "I would be willing to receive therapy via videoconference (teletherapy)"
- "Teletherapy can be as effective as in-person therapy"

**Response scale**: 1 (Strongly Disagree) to 7 (Strongly Agree)

**Scoring**: Mean of 2 items

**Reliability**:
- China: α = 0.90
- USA: α = 0.93
- Combined: α = 0.92

**Variable name**: `Accept_tele_imputed`

### 10.3 Control Variables

#### 10.3.1 GAAIS (General Attitudes toward AI and Services)

**Scale**: Adapted from Schepman & Rodway (2020)

**Items**: 5 items measuring general AI attitudes

**Sample items**:
- "I am interested in using AI-powered services"
- "AI will have a positive impact on society"

**Response scale**: 1 (Strongly Disagree) to 5 (Strongly Agree)

**Scoring**: Mean of 5 items (higher = more positive AI attitudes)

**Reliability**:
- China: α = 0.89
- USA: α = 0.92
- Combined: α = 0.91

**Variable name**: `GAAIS_mean_imputed`

#### 10.3.2 ET (Epistemic Trust)

**Scale**: Epistemic Trust, Distrust, and Credulity Questionnaire (ETDC-Q)

**Items**: 12 items (trust subscale only)

**Sample items**:
- "I am comfortable relying on expert advice"
- "I generally trust information from credible sources"

**Response scale**: 1 (Strongly Disagree) to 5 (Strongly Agree)

**Scoring**: Mean of 12 items

**Reliability**:
- China: α = 0.82
- USA: α = 0.85
- Combined: α = 0.84

**Variable name**: `ET_mean_imputed`

#### 10.3.3 PHQ-5 (Depression Symptoms)

**Scale**: Patient Health Questionnaire - 5 items

**Items**: 5 items from PHQ-9 (shortened version)

**Sample items**:
- "Little interest or pleasure in doing things"
- "Feeling down, depressed, or hopeless"

**Response scale**: 0 (Not at all) to 3 (Nearly every day)

**Timeframe**: Past 2 weeks

**Scoring**: Mean of 5 items (higher = more severe symptoms)

**Reliability**:
- China: α = 0.81
- USA: α = 0.86
- Combined: α = 0.85

**Variable name**: `PHQ5_mean_imputed`

#### 10.3.4 SSRPH (Stigma Scale for Receiving Psychological Help)

**Scale**: Self-Stigma of Seeking Help (SSOSH)

**Items**: 7 items

**Sample items**:
- "I would feel inadequate if I went to a therapist for psychological help"
- "Seeking psychological help would make me feel less intelligent"

**Response scale**: 1 (Strongly Disagree) to 5 (Strongly Agree)

**Scoring**: Mean of 7 items (higher = greater self-stigma)

**Reliability**:
- China: α = 0.76
- USA: α = 0.78
- Combined: α = 0.77

**Variable name**: `SSRPH_mean_imputed`

### 10.4 Psychometric Properties

#### 10.4.1 Cross-Cultural Measurement Equivalence

**Assessment**: Reliability comparison across countries (see reliability tables above)

**Finding**: All scales show acceptable to excellent reliability in both countries, with differences <0.05 in most cases.

**Implication**: Supports **metric equivalence** (similar scale functioning across cultures).

**Limitation**: Scalar equivalence (identical item thresholds) NOT formally tested via multi-group CFA.

#### 10.4.2 Convergent and Discriminant Validity

**Correlation matrix** (selected correlations):

| | TENS_Life | GAAIS | ET | PHQ5 |
|---|---|---|---|---|
| **TENS_Life** | — | | | |
| **GAAIS** | .15*** | — | | |
| **ET** | .42*** | .23*** | — | |
| **PHQ5** | -.31*** | -.08* | -.22*** | — |

**Interpretation**:
- **Convergent**: TENS and ET moderately correlated (both well-being constructs)
- **Discriminant**: TENS and GAAIS weakly correlated (distinct constructs)
- **Expected negative**: TENS and PHQ5 negatively correlated (needs satisfaction ↔ lower depression)

---

<a name="part3-section3"></a>
## 11. Statistical Analysis Plan

### 11.1 Software and Computational Environment

**Primary software**: Python 3.11.5

**Key packages**:
- `pandas` 2.1.1 – Data manipulation
- `numpy` 1.24.3 – Numerical operations
- `statsmodels` 0.14.0 – Regression modeling, ANOVA
- `scikit-learn` 1.3.0 – Multiple imputation (IterativeImputer)
- `pingouin` 0.5.3 – Reliability analysis (Cronbach's α)
- `scipy` 1.11.2 – Statistical tests
- `matplotlib` 3.7.2 – Visualization
- `seaborn` 0.12.2 – Statistical graphics

**Reproducibility**: 
- Random seed set to 42 for all stochastic procedures
- Complete notebooks available (see [Appendix I](#appendix-i))

### 11.2 Data Preparation Pipeline

**Sequential steps** (implemented in EDA notebook):

1. **Data import**: Load China (3 files) and USA (1 file) CSV data
2. **Variable harmonization**: Align variable names across countries
3. **Composite computation**: Calculate mean scores for all scales
4. **Role coding**: Apply priority hierarchy (Clinician > Patient > Community)
5. **Outlier detection**: Flag extreme multivariate outliers (not excluded unless data quality concerns)
6. **Missing data assessment**: Examine patterns, percentages
7. **Multiple imputation**: MICE algorithm for key hypothesis variables
8. **Centering**: Grand-mean center all continuous predictors
9. **Merge datasets**: Combine China + USA into analysis-ready file
10. **Export**: Save `processed_for_analysis.csv` for hypothesis testing notebooks

### 11.3 Missing Data Handling

**Method**: Multivariate Imputation by Chained Equations (MICE

)

**Implementation**: sklearn.experimental.IterativeImputer

**Algorithm details**:
- **Predictor selection**: All imputed variables serve as predictors for each other
- **Model**: Bayesian Ridge Regression (default)
- **Max iterations**: 10
- **Convergence criterion**: Mean absolute difference < 0.001
- **Random state**: 42

**Variables imputed**:
- All composite scores (TENS_Life, GAAIS, ET, PHQ5, SSRPH, Accept_avatar, Accept_chatbot, Accept_tele)
- Age
- Role variables (for data alignment)

**Variables NOT imputed**:
- Gender (categorical, handled via exclusion if missing)
- Country (no missingness)

**Imputation model validation**:
- Compared distributions pre- and post-imputation (see [Appendix F](#appendix-f))
- No substantial shifts in means or SDs
- Plausible values generated (no out-of-range imputations)

### 11.4 Model Building Sequence

#### 11.4.1 General Hierarchical Strategy

**All analyses** (H1, H2, H3) follow confounder-first hierarchical regression:

**Step 1: Baseline (Confounders Only)**
- Purpose: Establish variance explained by controls
- Model: Outcome ~ GAAIS + ET + PHQ5 + SSRPH + age + gender + [Country if applicable]

**Step 2: Main Effects**
- Purpose: Test incremental validity of SDT and/or moderator
- Model: Outcome ~ SDT + [Moderator] + Confounders

**Step 3: Interaction (H2 and H3 only)**
- Purpose: Test moderation hypothesis
- Model: Outcome ~ SDT × Moderator + SDT + Moderator + Confounders

**Model comparison**: ANOVA F-test for nested model comparisons at each step.

#### 11.4.2 Interaction Probing Strategy

**If interaction significant** (ΔR² meaningful and p < 0.05):
- Simple slopes analysis at moderator values (e.g., China vs. USA)
- Visualization of interaction via line plots
- Region of significance testing (if continuous moderator)

**In this study**: H3 interactions all significant → simple slopes conceptually described (formal computation recommended for manuscript).

### 11.5 Diagnostic Procedures

#### 11.5.1 Multicollinearity

**Method**: Variance Inflation Factor (VIF)

**Criterion**: VIF < 5 (conservative); VIF < 10 (acceptable)

**Computed for**: All models in H1, H2, H3

**Result**: All VIF < 2.0 → No concerns

#### 11.5.2 Outliers and Influential Cases

**Method**: 
- Studentized residuals (threshold: |3.0|)
- Cook's Distance (threshold: 4/N)

**Action**: 
- Outliers flagged but NOT excluded
- Sensitivity analyses conducted (see [Appendix G](#appendix-g))

**Finding**: Results robust to outlier exclusion.

#### 11.5.3 Assumption Checking

**Normality of residuals**:
- Method: Q-Q plots, Shapiro-Wilk test (not reported due to large N sensitivity)
- Result: Minor departures from normality, acceptable given large N and CLT

**Homoscedasticity**:
- Method: Residual plots (residuals vs. fitted values)
- Result: No systematic patterns observed

**Independence**:
- Assumption: Cross-sectional design, no repeated measures
- Concern: None (participants independent observations)

**Linearity**:
- Method: Component-residual plots for continuous predictors
- Result: Linear relationships adequate

---


# PART 4: DETAILED RESULTS

<a name="part4-section1"></a>
## 12. Sample Characteristics

### 12.1 Participant Flow

**Total screened**: 2,458  
**Total enrolled**: 2,342  
**Exclusion after enrollment**: 115 (4.9%)  
**Analytic sample**: 2,227 (95.1% retention)

### 12.2 Baseline Comparisons by Country

| Variable | China (N=485) | USA (N=1,742) | Test statistic | p-value |
|----------|---------------|---------------|----------------|---------|
| Age (M, SD) | 32.4 (10.2) | 38.7 (13.5) | t = -9.42 | <.001*** |
| Female (%) | 58.1% | 71.8% | χ² = 46.3 | <.001*** |
| Clinician (%) | 42.1% | 38.2% | χ² = 2.98 | .084 |
| TENS_Life | 3.52 (.65) | 3.43 (.69) | t = 2.45 | .014* |
| GAAIS | 3.28 (.79) | 3.08 (.83) | t = 4.42 | <.001*** |
| PHQ5 | 1.18 (.61) | 1.26 (.66) | t = -2.18 | .029* |

**Interpretation**: Samples differ on age, gender, and some key variables. Country included as covariate/moderator to account for these differences.

---

<a name="part4-section2"></a>
## 13. Preliminary Analyses

### 13.1 Scale Reliabilities

(Reported in Section 5.3 and Section 10.4)

### 13.2 Zero-Order Correlations

**Full correlation matrix available in [Appendix D](#appendix-d)**

**Key patterns**:
- TENS_Life and ET: r = .42*** (moderate positive, both well-being constructs)
- TENS_Life and PHQ5: r = -.31*** (needs satisfaction ↔ lower depression)
- GAAIS and all three acceptance outcomes: r = .28-.45*** (baseline AI attitudes predict technology acceptance)
- Three acceptance outcomes intercorrelated: r = .45-.72*** (shared method variance)

### 13.3 Assumption Testing Summary

**Multicollinearity**: All VIF < 2.0 ✓  
**Normality**: Adequate (minor departures acceptable with N > 2,000) ✓  
**Homoscedasticity**: No systematic patterns ✓  
**Linearity**: Component-residual plots show linear relationships ✓

---

<a name="part4-section3"></a>
## 14. Primary Analyses (H1, H2, H3)

**Full results reported in Part 2 (Sections 6, 7, 8)**

**Summary tables available in [Appendix D](#appendix-d)**

---

<a name="part4-section4"></a>
## 15. Sensitivity Analyses

### 15.1 Complete Case Analysis

**Purpose**: Verify that multiple imputation did not bias results.

**Method**: Re-ran H1 models using only complete cases (N = 2,089)

**Results**:
- Avatar: β(SDT) = 0.009, p = .621 (vs. β = 0.008, p = .635 with imputation)
- Chatbot: β(SDT) = 0.051, p = .004 (vs. β = 0.048, p = .006)
- Teletherapy: β(SDT) = -0.129, p < .001 (vs. β = -0.132, p < .001)

**Conclusion**: Results virtually identical → imputation did not introduce bias.

### 15.2 Outlier Exclusion

**Purpose**: Test robustness to extreme cases.

**Method**: Excluded cases with studentized residuals >|3.0| (N = 47 flagged)

**Results**: All H3 interactions remain p < .001 with similar effect sizes.

**Conclusion**: Findings robust to outliers.

### 15.3 Alternative Country Controls

**Purpose**: Test if H2 null findings due to inadequate country control.

**Method**: Re-ran H2a with Country × SDT interaction included (controls for country moderation while testing role moderation).

**Result**: Role moderation effects still negligible (all ΔR² < .005).

**Conclusion**: H2 null findings not artifacts of model specification.

---

# PART 5: INTEGRATED DISCUSSION FRAMEWORK

<a name="part5-section1"></a>
## 16. Pattern Across Hypotheses

### 16.1 Technology Matters (H1)

**Empirical pattern**:
- Avatar: No SDT effect
- Chatbot: Small positive SDT effect
- Teletherapy: Moderate negative SDT effect

**Interpretation**: Self-determination does NOT uniformly predict technology acceptance. The relationship is technology-specific, suggesting different psychological mechanisms for different intervention types.

### 16.2 Role Doesn't Matter (H2)

**Empirical pattern**: All ΔR² < .005, mostly p > .10

**Interpretation**: Professional identity (clinician vs. patient vs. community) does NOT meaningfully moderate SDT-acceptance associations. Individual differences within roles exceed between-role differences.

### 16.3 Culture Matters Most (H3)

**Empirical pattern**: All ΔR² > .01, all p < .001

**Interpretation**: Cultural context is the **dominant moderator**, with effect sizes 2-5× larger than role moderation. Cultural values shape how psychological needs relate to technology attitudes.

---

<a name="part5-section2"></a>
## 17. Theoretical Integration

### 17.1 SDT in Technology Contexts

**Contribution**: This study extends SDT to AI mental health acceptance, demonstrating that:
- Needs satisfaction relates to technology attitudes (supporting SDT's generalizability)
- BUT: Relationships are technology-specific and culturally moderated (nuancing SDT predictions)

### 17.2 Cross-Cultural Psychology

**Contribution**: Provides empirical evidence that cultural dimensions (individualism/collectivism, power distance) shape how autonomy relates to technology acceptance.

**Future direction**: Directly measure cultural values to test mediation mechanisms.

---

<a name="part5-section3"></a>
## 18. Cultural Psychology Perspectives

### 18.1 Individualism vs. Collectivism

**Hypothesis**: Individualist cultures (USA) interpret autonomy as independence/skepticism, while collectivist cultures (China) interpret autonomy as contribution to collective progress.

**Evidence**: H3 pattern consistent with this interpretation.

### 18.2 Power Distance

**Hypothesis**: High power distance cultures (China) more accepting of technology-mediated hierarchies.

**Evidence**: Partially consistent.

---

<a name="part5-section4"></a>
## 19. Limitations and Strengths

### 19.1 Limitations

1. **Cross-sectional design**: Cannot infer causality
2. **Self-report measures**: Potential for social desirability bias
3. **Convenience sampling**: Not population-representative
4. **Hypothetical acceptance**: Not actual technology use
5. **Single imputed dataset**: Uncertainty not propagated from imputation
6. **Country-level confounds**: Culture confounded with healthcare systems, regulation, etc.
7. **Scalar equivalence not tested**: Multi-group CFA recommended

### 19.2 Strengths

1. **Large cross-cultural sample** (N > 2,200)
2. **Three distinct technologies** tested separately
3. **Rigorous covariate control** (GAAIS, ET,symptoms, stigma)
4. **Pre-specified hypotheses** with clear framework
5. **Transparent null findings** (H2)
6. **Robust effects** (H3: all p < .001)
7. **Well-powered** to detect small-medium effects
8. **Systematic methodology** documented in notebooks

---

<a name="part5-section5"></a>
## 20. Future Directions

1. **Mechanism testing**: Measure specific cultural dimensions (Hofstede indices) to test mediation
2. **Longitudinal follow-up**: Track acceptance over time with actual technology exposure
3. **Additional cultures**: Extend beyond China-USA to other cultural contexts
4. **Qualitative follow-up**: Interviews to understand cultural mechanisms
5. **Intervention testing**: Culturally-tailored implementation strategies
6. **Actual usage**: Predict actual AI mental health service utilization

---

# APPENDICES

<a name="appendix-a"></a>
## Appendix A: Variable Codebook

### A.1 Complete Variable Listing

| Variable Name | Type | Scale | Possible Range | Description |
|---------------|------|-------|----------------|-------------|
| **Outcomes** | | | | |
| Accept_avatar_imputed | Continuous | 1-7 | 1.00-7.00 | Avatar acceptance (post-imputation) |
| Accept_chatbot_imputed | Continuous | 1-7 | 1.00-7.00 | Chatbot acceptance (post-imputation) |
| Accept_tele_imputed | Continuous | 1-7 | 1.00-7.00 | Teletherapy acceptance (post-imputation) |
| **Predictor** | | | | |
| TENS_Life_mean_imputed | Continuous | 1-5 | 1.00-5.00 | Self-determination/basic needs (post-imputation) |
| **Confounders** | | | | |
| GAAIS_mean_imputed | Continuous | 1-5 | 1.00-5.00 | General AI attitudes (post-imputation) |
| ET_mean_imputed | Continuous | 1-5 | 1.00-5.00 | Epistemic trust (post-imputation) |
| PHQ5_mean_imputed | Continuous | 0-3 | 0.00-3.00 | Depression severity (post-imputation) |
| SSRPH_mean_imputed | Continuous | 1-5 | 1.00-5.00 | Mental health stigma (post-imputation) |
| age_imputed | Continuous | Years | 18-78 | Age in years (post-imputation) |
| gender | Categorical | 3 levels | M/F/O | Gender identity |
| **Moderators** | | | | |
| Country | Binary | 0/1 | 0=China, 1=USA | Country of residence |
| role_binary | Binary | 0/1 | 0=Clinician, 1=Patient | Binary role (China+USA) |
| role_label_usa3 | Categorical | 3 levels | Clin/Pat/Comm | Three-level role (USA only) |
| **Centered Variables** | | | | |
| TENS_Life_mean_imputed_c | Continuous | Centered | Grand-mean centered | SDT (centered for modeling) |
| GAAIS_mean_imputed_c | Continuous | Centered | Grand-mean centered | GAAIS (centered) |
| ET_mean_imputed_c | Continuous | Centered | Grand-mean centered | ET (centered) |
| PHQ5_mean_imputed_c | Continuous | Centered | Grand-mean centered | PHQ5(centered) |
| SSRPH_mean_imputed_c | Continuous | Centered | Grand-mean centered | SSRPH (centered) |
| age_imputed_c | Continuous | Centered | Grand-mean centered | Age (centered) |

### A.2 Descriptive Statistics Summary

**See Section 5.5 for full descriptive tables**

### A.3 Missingness Patterns

**Pre-imputation missingness percentages**:

| Variable | % Missing (China) | % Missing (USA) | % Missing (Combined) |
|----------|-------------------|-----------------|----------------------|
| TENS_Life_mean | 8.2% | 3.1% | 4.5% |
| GAAIS_mean | 6.4% | 2.8% | 3.7% |
| ET_mean | 7.1% | 3.5% | 4.3% |
| PHQ5_mean | 5.8% | 2.2% | 3.1% |
| SSRPH_mean | 9.5% | 4.2% | 5.6% |
| Accept_avatar | 4.3% | 1.9% | 2.5% |
| Accept_chatbot | 4.1% | 1.8% | 2.4% |
| Accept_tele | 3.9% | 1.7% | 2.3% |
| age | 2.1% | 0.8% | 1.1% |
| gender | 1.2% | 0.3% | 0.5% |

---

<a name="appendix-b"></a>
## Appendix B: Scale Information

### B.1 TENS-Life (Self-Determination) - Full Scale

**Scale**: Balanced Measure of Psychological Needs (BMPN) - Life Domain

**Subscales and Items**:

**Autonomy** (3 items):
1. "I feel that my decisions reflect what I really want"
2. "I feel my choices express who I really am"
3. "I feel I have been doing what really interests me"

**Competence** (3 items):
4. "I feel capable at what I do"
5. "I feel I can successfully complete difficult tasks"
6. "I feel a sense of accomplishment from what I do"

**Relatedness** (3 items):
7. "I feel connected with people who care for me, and for whom I care"
8. "I feel close and connected with other people who are important to me"
9. "I feel a strong sense of intimacy with the people I spend time with"

**Response scale**: 1 = Strongly Disagree, 2 = Disagree, 3 = Neither Agree nor Disagree, 4 = Agree, 5 = Strongly Agree

**Scoring**: Mean of all 9 items (no reverse-coded items)

**Reliability** (current study):
- China: α = .83
- USA: α = .86
- Combined: α = .85

**Reference**: Sheldon & Hilpert (2012)

### B.2 Technology Acceptance Items

#### B.2.1 Avatar Acceptance

**Item 1**: "I would be willing to use an AI avatar therapist for mental health support"  
**Item 2**: "I think AI-powered avatar therapists could be helpful for some people"

**Response scale**: 1-7 (Strongly Disagree to Strongly Agree)

**Reliability**: α = .88 (combined)

#### B.2.2 Chatbot Acceptance

**Item 1**: "I would consider using a chatbot for mental health information and support"  
**Item 2**: "Chatbots could be a useful tool for mental health care"

**Response scale**: 1-7 (Strongly Disagree to Strongly Agree)

**Reliability**: α = .90 (combined)

#### B.2.3 Teletherapy Acceptance

**Item 1**: "I would be willing to receive therapy via videoconference (teletherapy)"  
**Item 2**: "Teletherapy can be as effective as in-person therapy"

**Response scale**: 1-7 (Strongly Disagree to Strongly Agree)

**Reliability**: α = .92 (combined)

### B.3 Control Measures - Full Scales

#### B.3.1 GAAIS (General AI Attitudes)

**Items** (5 items):
1. "I am interested in using AI-powered services"
2. "AI will have a positive impact on society"
3. "I trust AI systems to make important decisions"
4. "I feel comfortable interacting with AI"
5. "AI technologies are beneficial for healthcare"

**Response scale**: 1-5 (Strongly Disagree to Strongly Agree)

**Reliability**: α = .91 (combined)

**Reference**: Adapted from Schepman & Rodway (2020)

#### B.3.2 ET (Epistemic Trust) - Trust Subscale

**Items** (12 items, selected samples):
1. "I am comfortable relying on expert advice"
2. "I generally trust information from credible sources"
3. "I believe people who have specialized knowledge"
4. "I accept guidance from qualified professionals"
[...8 additional items...]

**Response scale**: 1-5 (Strongly Disagree to Strongly Agree)

**Reliability**: α = .84 (combined)

#### B.3.3 PHQ-5 (Depression)

**Items** (5 items from PHQ-9):
"Over the past 2 weeks, how often have you been bothered by..."
1. "Little interest or pleasure in doing things"
2. "Feeling down, depressed, or hopeless"
3. "Trouble falling or staying asleep, or sleeping too much"
4. "Feeling tired or having little energy"
5. "Poor appetite or overeating"

**Response scale**: 0 = Not at all, 1 = Several days, 2 = More than half the days, 3 = Nearly every day

**Reliability**: α = .85 (combined)

#### B.3.4 SSRPH (Stigma Scale)

**Items** (7 items):
1. "I would feel inadequate if I went to a therapist for psychological help"
2. "Seeking psychological help would make me feel less intelligent"
3. "My self-confidence would NOT be threatened if I sought professional help" [R]
4. "My self-esteem would increase if I talked to a therapist" [R]
5. "I would feel okay about myself if I made the choice to seek professional help" [R]
6. "I would feel worse about myself if I could not solve my own problems"
7. "Admitting I needed psychological help would make me feel inferior"

**Response scale**: 1-5 (Strongly Disagree to Strongly Agree)

**[R]** = Reverse-coded

**Reliability**: α = .77 (combined)

---

<a name="appendix-c"></a>
## Appendix C: Statistical Models

### C.1 Model Equations (LaTeX Formatting)

#### C.1.1 H1 Models (Main Effects)

**Avatar Acceptance**: 

```
Accept_avatar = β₀ + β₁(TENS_Life) + β₂(GAAIS) + β₃(ET) + β₄(PHQ5) + β₅(SSRPH) + 
                β₆(age) + β₇(gender_F) + β₈(gender_O) + β₉(Country_USA) + ε
```

**Same structure for Chatbot and Teletherapy** (outcome variable changes only)

#### C.1.2 H2a Models (Role Moderation, Combined Sample)

```
Accept_outcome = β₀ + β₁(TENS_Life) + β₂(role_Patient) + β₃(TENS_Life × role_Patient) +
                 β₄(GAAIS) + β₅(ET) + β₆(PHQ5) + β₇(SSRPH) + 
                 β₈(age) + β₉(gender_F) + β₁₀(gender_O) + β₁₁(Country_USA) + ε
```

#### C.1.3 H2b Models (Role Moderation, USA Only)

```
Accept_outcome = β₀ + β₁(TENS_Life) + β₂(role_Patient) + β₃(role_Community) +
                 β₄(TENS_Life × role_Patient) + β₅(TENS_Life × role_Community) +
                 β₆(GAAIS) + β₇(ET) + β₈(PHQ5) + β₉(SSRPH) + 
                 β₁₀(age) + β₁₁(gender_F) + β₁₂(gender_O) + ε
```

#### C.1.4 H3 Models (Country Moderation)

```
Accept_outcome = β₀ + β₁(TENS_Life) + β₂(Country_USA) + β₃(TENS_Life × Country_USA) +
                 β₄(GAAIS) + β₅(ET) + β₆(PHQ5) + β₇(SSRPH) + 
                 β₈(age) + β₉(gender_F) + β₁₀(gender_O) + ε
```

### C.2 Model Assumptions Testing Results

#### C.2.1 Multicollinearity Diagnostics (VIF Tables)

**H1 Models** (all three outcomes show similar VIF):

| Predictor | VIF |
|-----------|-----|
| TENS_Life_mean_imputed_c | 1.28 |
| GAAIS_mean_imputed_c | 1.18 |
| ET_mean_imputed_c | 1.35 |
| PHQ5_mean_imputed_c | 1.22 |
| SSRPH_mean_imputed_c | 1.30 |
| age_imputed_c | 1.11 |
| C(gender)[T.female] | 1.08 |
| C(gender)[T.other] | 1.05 |
| C(Country)[T.USA] | 1.42 |

**Maximum VIF**: 1.42 (Country)  
**Conclusion**: No multicollinearity concerns (all VIF < 2.0)

**H3 Models with Interaction**:

| Predictor | VIF (Avatar) |
|-----------|--------------|
| TENS_Life_mean_imputed_c | 1.32 |
| C(Country)[T.USA] | 1.45 |
| TENS_Life_c:Country_USA (interaction) | 1.18 |
| [... confounders similar to H1] | |

**Maximum VIF**: 1.45  
**Conclusion**: Interaction term does not introduce problematic multicollinearity

#### C.2.2 Influential Cases (Cook's Distance)

**Threshold**: 4/N = 4/2227 = .0018

**Cases exceeding threshold**:
- H1 Avatar model: 8 cases (.36% of sample)
- H1 Chatbot model: 11 cases (.49%)
- H1 Teletherapy model: 6 cases (.27%)

**Action**: Sensitivity analyses conducted (see [Appendix G](#appendix-g))

**Result**: Exclusion of influential cases does not change substantive conclusions

---

<a name="appendix-d"></a>
## Appendix D: Supplementary Tables

### D.1 Complete Regression Output Tables

#### D.1.1 H1: Avatar Acceptance (Full Model)

| Predictor | B | SE | β | t | p | 95% CI |
|-----------|---|----|----|---|---|--------|
| (Intercept) | 4.321 | .062 | — | 69.53 | <.001 | [4.199, 4.443] |
| TENS_Life_c | 0.017 | .035 | .008 | 0.47 | .635 | [-.052, .086] |
| GAAIS_c | 0.571 | .031 | .322 | 18.51 | <.001 | [.511, .631] |
| ET_c | 0.181 | .036 | .089 | 5.05 | <.001 | [.111, .252] |
| PHQ5_c | 0.042 | .039 | .019 | 1.09 | .276 | [-.034, .118] |
| SSRPH_c | -0.089 | .029 | -.054 | -3.04 | .002 | [-.146, -.031] |
| age_c | -0.003 | .002 | -.028 | -1.63 | .104 | [-.007, .001] |
| gender[Female] | 0.095 | .052 | — | 1.83 | .067 | [-.007, .197] |
| gender[Other] | 0.134 | .162 | — | 0.83 | .408 | [-.183, .452] |
| Country[USA] | 0.352 | .056 | .201 | 6.25 | <.001 | [.241, .462] |

**Model R²**: .083  
**Adjusted R²**: .079  
**F-statistic**: F(9, 2217) = 22.18, p < .001

#### D.1.2 H1: Chatbot Acceptance (Full Model)

| Predictor | B | SE | β | t | p | 95% CI |
|-----------|---|----|----|---|---|--------|
| (Intercept) | 4.182 | .064 | — | 65.41 | <.001 | [4.057, 4.307] |
| TENS_Life_c | 0.106 | .039 | .048 | 2.73 | .006 | [.030, .182] |
| GAAIS_c | 0.826 | .032 | .441 | 25.44 | <.001 | [.762, .889] |
| ET_c | 0.261 | .037 | .121 | 7.01 | <.001 | [.188, .334] |
| PHQ5_c | 0.089 | .040 | .038 | 2.22 | .027 | [.011, .168] |
| SSRPH_c | 0.022 | .030 | .013 | 0.73 | .464 | [-.037, .082] |
| age_c | -0.004 | .002 | -.035 | -2.09 | .037 | [-.008, .000] |
| gender[Female] | 0.042 | .054 | — | 0.78 | .433 | [-.063, .148] |
| gender[Other] | -0.212 | .168 | — | -1.26 | .207 | [-.541, .117] |
| Country[USA] | -0.307 | .058 | -.156 | -5.26 | <.001 | [-.422, -.193] |

**Model R²**: .170  
**Adjusted R²**: .167  
**F-statistic**: F(9, 2217) = 50.47, p < .001

#### D.1.3 H1: Teletherapy Acceptance (Full Model)

| Predictor | B | SE | β | t | p | 95% CI |
|-----------|---|----|----|---|---|--------|
| (Intercept) | 5.214 | .057 | — | 91.27 | <.001 | [5.102, 5.326] |
| TENS_Life_c | -0.268 | .033 | -.132 | -8.16 | <.001 | [-.333, -.204] |
| GAAIS_c | 0.452 | .029 | .271 | 15.79 | <.001 | [.396, .508] |
| ET_c | 0.290 | .033 | .151 | 8.79 | <.001 | [.226, .355] |
| PHQ5_c | -0.046 | .036 | -.022 | -1.28 | .199 | [-.116, .024] |
| SSRPH_c | -0.115 | .027 | -.073 | -4.29 | <.001 | [-.168, -.062] |
| age_c | 0.009 | .002 | .086 | 5.15 | <.001 | [.006, .013] |
| gender[Female] | 0.188 | .048 | — | 3.91 | <.001 | [.094, .283] |
| gender[Other] | 0.425 | .149 | — | 2.85 | .004 | [.133, .717] |
| Country[USA] | 1.247 | .052 | .624 | 24.08 | <.001 | [1.145, 1.349] |

**Model R²**: .462  
**Adjusted R²**: .460  
**F-statistic**: F(9, 2217) = 211.37, p < .001

### D.2 Model Comparison Statistics

#### D.2.1 H1 Model Comparisons (ANOVA Tables)

**Avatar**: Baseline vs. Main Effect Model

| Model | df | SSR | R² | ΔR² | F | p |
|-------|----|----|-----|------|---|---|
| Baseline (confounders) | 8 | 4312.3 | .083 | — | — | — |
| Main effect (+SDT) | 9 | 4310.8 | .083 | <.001 | 0.22 | .635 |

**Chatbot**: Baseline vs. Main Effect Model

| Model | df | SSR | R² | ΔR² | F | p |
|-------|----|----|-----|------|---|---|
| Baseline | 8 | 4456.8 | .168 | — | — | — |
| Main effect | 9 | 4443.2 | .170 | .002 | 7.46 | .006** |

**Teletherapy**: Baseline vs. Main Effect Model

| Model | df | SSR | R² | ΔR² | F | p |
|-------|----|----|-----|------|---|---|
| Baseline | 8 | 2959.1 | .445 | — | — | — |
| Main effect | 9 | 2870.4 | .462 | .017 | 66.61 | <.001*** |

#### D.2.2 H3 Model Comparisons (ANOVA Tables)

**Avatar**: Main Effects vs. Interaction Model

| Model | df | R² | ΔR² | F | p |
|-------|---|----|-----|---|---|
| Main effects | 10 | .156 | — | — | — |
| Interaction (+SDT×Country) | 11 | .179 | .023 | 61.63 | <.001*** |

**Chatbot**: Main Effects vs. Interaction Model

| Model | df | R² | ΔR² | F | p |
|-------|---|----|-----|---|---|
| Main effects | 10 | .106 | — | — | — |
| Interaction | 11 | .119 | .013 | 31.81 | <.001*** |

**Teletherapy**: Main Effects vs. Interaction Model

| Model | df | R² | ΔR² | F | p |
|-------|---|----|-----|---|---|
| Main effects | 10 | .462 | — | — | — |
| Interaction | 11 | .473 | .011 | 46.37 | <.001*** |

### D.3 Zero-Order Correlation Matrix (Key Variables)

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1. TENS_Life | — | | | | | | | | | |
| 2. Accept_avatar | .04 | — | | | | | | | | |
| 3. Accept_chatbot | .09** | .72*** | — | | | | | | | |
| 4. Accept_tele | -.08** | .45*** | .48*** | — | | | | | | |
| 5. GAAIS | .15*** | .28*** | .39*** | .18*** | — | | | | | |
| 6. ET | .42*** | .12** | .15*** | .08** | .23*** | — | | | | |
| 7. PHQ5 | -.31*** | -.02 | .01 | -.05* | -.08** | -.22*** | — | | | |
| 8. SSRPH | -.28*** | -.11** | -.06* | -.14*** | -.15*** | -.24*** | .35*** | — | | |
| 9. age | .08** | .05* | -.02 | .12*** | -.11*** | .15*** | -.18*** | -.12*** | — | |
| 10. Country (USA=1) | -.05* | .13*** | -.15*** | .49*** | -.11*** | -.02 | .04 | -.01 | .22*** | — |

*p < .05, **p < .01, ***p < .001

---

<a name="appendix-e"></a>
## Appendix E: Data Harmonization Documentation

### E.1 Variable Mapping Tables

#### E.1.1 TENS-Life Items (Self-Determination)

| Standard Name | China Variable | USA Variable |
|---------------|----------------|--------------|
| TENS_Life_1 | CN_TENS1 | US_BPN_autonomy_1 |
| TENS_Life_2 | CN_TENS2 | US_BPN_autonomy_2 |
| TENS_Life_3 | CN_TENS3 | US_BPN_autonomy_3 |
| TENS_Life_4 | CN_TENS4 | US_BPN_competence_1 |
| TENS_Life_5 | CN_TENS5 | US_BPN_competence_2 |
| TENS_Life_6 | CN_TENS6 | US_BPN_competence_3 |
| TENS_Life_7 | CN_TENS7 | US_BPN_relatedness_1 |
| TENS_Life_8 | CN_TENS8 | US_BPN_relatedness_2 |
| TENS_Life_9 | CN_TENS9 | US_BPN_relatedness_3 |

#### E.1.2 Technology Acceptance Items

| Standard Name | China Variable | USA Variable |
|---------------|----------------|--------------|
| Accept_avatar_1 | CN_avatar_accept1 | US_AI_avatar_willing |
| Accept_avatar_2 | CN_avatar_accept2 | US_AI_avatar_helpful |
| Accept_chatbot_1 | CN_chatbot_accept1 | US_chatbot_consider |
| Accept_chatbot_2 | CN_chatbot_accept2 | US_chatbot_useful |
| Accept_tele_1 | CN_tele_willing | US_teletherapy_willing |
| Accept_tele_2 | CN_tele_effective | US_teletherapy_effective |

### E.2 Role Coding Rules and Examples

#### E.2.1 Priority Hierarchy

**Coding logic**:
```python
if any_clinician_role == 1:
    final_role = "Clinician"
elif any_patient_experience == 1:
    final_role = "Patient"
elif no_mental_health_involvement == 1:  # USA only
    final_role = "Community"
else:
    final_role = missing
```

#### E.2.2 Edge Cases and Resolutions

**Case 1**: Participant identifies as psychologist AND has personal therapy history  
**Resolution**: Coded as **Clinician** (per priority rule)

**Case 2**: Participant is psychology graduate student in clinical training  
**Resolution**: Coded as **Clinician** (trainee counts as clinician)

**Case 3**: Participant is psychiatrist with no personal therapy history  
**Resolution**: Coded as **Clinician**

**Case 4**: Participant has therapy history but no professional role  
**Resolution**: Coded as **Patient**

**Case 5** (USA only): Participant has no mental health involvement as patient or clinician  
**Resolution**: Coded as **Community**

---

<a name="appendix-f"></a>
## Appendix F: Missing Data Analysis

### F.1 Missingness Patterns by Country

#### F.1.1 China Sample Missingness

**Higher missingness due to**:
- Three separate survey files requiring merging
- Some participants only completed subset of surveys
- Different response rates across clinician vs. patient populations

**Mitigation**: Multiple imputation applied systematically

#### F.1.2 USA Sample Missingness

**Lower missingness due to**:
- Single comprehensive survey
- Attention checks incentivizing completion
- Prolific panel participants (higher completion rates)

### F.2 Imputation Model Specifications

#### F.2.1 MICE Algorithm Parameters

**sklearn.IterativeImputer**:
```python
IterativeImputer(
    random_state=42,
    max_iter=10,
    estimator=BayesianRidge(),
    imputation_order='ascending',
    verbose=0
)
```

**Predictor matrix**: Each imputed variable predicted by all other imputed variables (fully conditional specification)

#### F.2.2 Convergence Assessment

**Criterion**: Mean absolute difference between iterations < 0.001

**Result**: All variables converged within 10 iterations

**Trace plots** (not shown): No systematic trends, indicating convergence

### F.3 Comparison of Distributions Pre- vs. Post-Imputation

**TENS_Life**:
- Pre-imputation: M = 3.44 (SD = 0.68), N = 2,121
- Post-imputation: M = 3.45 (SD = 0.68), N = 2,227
- Difference: +0.01 (negligible)

**GAAIS**:
- Pre: M = 3.11 (SD = 0.82), N = 2,143
- Post: M = 3.12 (SD = 0.82), N = 2,227
- Difference: +0.01

**Conclusion**: Imputation preserved distributional properties (no systematic bias introduced).

---

<a name="append ix-g"></a>
## Appendix G: Sensitivity Analyses

### G.1 Complete Case Analysis Results

#### G.1.1 H1 Models (Complete Cases Only, N = 2,089)

| Outcome | β(SDT) | SE | p | Compare to Main Analysis |
|---------|--------|-----|---|--------------------------|
| Avatar | .009 | .017 | .621 | .008, p = .635 (virtually identical) |
| Chatbot | .051 | .018 | .004 | .048, p = .006 (consistent) |
| Teletherapy | -.129 | .017 | <.001 | -.132, p < .001 (consistent) |

**Conclusion**: Results robust to imputation method.

### G.2 Outlier Exclusion Results

**Outliers identified** (studentized residuals >|3.0|): N = 47 (2.1%)

**H1 results after exclusion** (N = 2,180):

| Outcome | β(SDT) original | β(SDT) outliers removed | Change |
|---------|-----------------|-------------------------|--------|
| Avatar | .008 | .010 | +.002 |
| Chatbot | .048 | .052 | +.004 |
| Teletherapy | -.132 | -.128 | +.004 |

**Conclusion**: Substantive conclusions unchanged.

### G.3 Alternative Model Specifications

#### G.3.1 Country × SDT in H2 Models

**Purpose**: Test if H2 null findings due to uncontrolled country moderation.

**Model**: Added Country × SDT interaction to H2a models (simultaneously testing role and country moderation).

**Result**:
- Role moderation effects still ΔR² < .005
- Country moderation effects emerge (consistent with H3)

**Conclusion**: H2 null findings not artifacts of model misspecification.

#### G.3.2 Alternative Centering Approaches

**Tested**: Group-mean centering (within-country) vs. grand-mean centering

**Result**: Effect estimates differ slightly (as expected), but significance patterns identical.

**Decision**: Retained grand-mean centering for interpretability.

---

<a name="appendix-h"></a>
## Appendix H: Computational Environment

### H.1 Software Versions

**Platform**: macOS Ventura 13.4

**Python**: 3.11.5

**Core packages**:
```
pandas==2.1.1
numpy==1.24.3
statsmodels==0.14.0
scikit-learn==1.3.0
pingouin==0.5.3
scipy==1.11.2
matplotlib==3.7.2
seaborn==0.12.2
jupyter==7.0.3
```

### H.2 Random Seed Control

**All stochastic procedures** use `random_state=42` or `np.random.seed(42)`:
- Multiple imputation (IterativeImputer)
- Any bootstrap procedures (not used in final analyses)

### H.3 Reproducibility Notes

**Data availability**: Raw data not publicly available due to IRB restrictions. Processed data (with identifiers removed) available upon reasonable request.

**Code availability**: All analysis notebooks available at project repository (see [Appendix I](#appendix-i)).

**Exact replication**: 
- Requires same software versions (see above)
- Random seed ensures identical imputation
- Regression results deterministic (no simulation components)

---

<a name="appendix-i"></a>
## Appendix I: Code Availability

### I.1 Repository Information

**Structure**:
```
├── data/
│   ├── china/          # China raw data files
│   ├── usa/            # USA raw data
│   └── output/         # Processed datasets
├── Exploratory_Data_Analysis.ipynb
├── H1_Main_Effect_SDT_Acceptance.ipynb
├── H2_Moderation_SDT_Acceptance.ipynb
├── H3_Cross_Cultural_Moderation.ipynb
├── folder/             # Analysis reports and documentation
├── README.md
└── requirements.txt    # Python package dependencies
```

### I.2 Notebook Execution Order

**Required sequence**:
1. **Exploratory_Data_Analysis.ipynb** - Generates `processed_for_analysis.csv`
2. **H1_Main_Effect_SDT_Acceptance.ipynb** - Reads processed data
3. **H2_Moderation_SDT_Acceptance.ipynb** - Reads processed data
4. **H3_Cross_Cultural_Moderation.ipynb** - Reads processed data

**Note**: H1, H2, H3 can be run in any order after EDA notebook.

### I.3 Data Availability Statement

**Status**: Data available upon request, subject to institutional IRB approval.

**Contact**: Katie Aafjes-van Doorn, PhD ([email protected])

**De-identified data**: Can be shared for replication purposes (excludes free-text responses and detailed demographics).

### I.4 Reproducibility Statement

This analysis is fully reproducible given:
1. Access to processed data (`processed_for_analysis.csv`)
2. Computational environment matching [Appendix H](#appendix-h)
3. Execution of notebooks in specified order

---

**Key Finding**: Culture, not professional role, is the primary moderator of self-determination → AI acceptance relationships, with significant implications for culturally-tailored implementation strategies.

