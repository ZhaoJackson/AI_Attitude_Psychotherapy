# AI Attitude Psychotherapy - SDT Analysis

**Predicting AI Acceptance in Mental Health Interventions through Self-Determination Theory: A Cross-Cultural Study**

Cross-cultural analysis (China-USA, N=2227) examining how self-determination theory predicts acceptance of three AI mental health technologies: avatar therapists, chatbots, and teletherapy.

**Principal Investigator**: Katie Aafjes-van Doorn, PhD (NYU Shanghai)  
**Analyst**: Jackson Zhao (Columbia University)  
**Status**: ✅ All analyses complete (Dec 2024)

---

## Project Overview

This study tests whether basic psychological needs satisfaction (self-determination theory) predicts acceptance of AI-assisted mental health interventions, and whether these relationships are moderated by clinical role and cultural context.

### Key Findings
- **H1 (Main Effects)**: Technology-specific patterns - SDT does not uniformly predict acceptance across all technologies
- **H2 (Role Moderation)**: NOT supported - Clinical role does not moderate SDT-acceptance relationships (ΔR²<0.005)
- **H3 (Country Moderation)**: STRONGLY supported - Culture is the primary moderator (all p<0.001, ΔR²=0.011-0.023)

**Primary Conclusion**: Cultural context, not professional role, fundamentally shapes how self-determination relates to AI acceptance.

---

## Repository Structure

### Analysis Notebooks (Run in Order)
1. **`Exploratory_Data_Analysis.ipynb`** 
   - Data harmonization (China + USA)
   - Variable construction and imputation
   - Role coding and sample preparation
   - Output: `data/output/processed_for_analysis.csv`

2. **`H1_Main_Effect_SDT_Acceptance.ipynb`**
   - H1: SDT predicts acceptance × 3 technologies
   - Confounder-first modeling approach
   - Results: Technology-specific effects (Avatar: ns, Chatbot: small +, Teletherapy: moderate -)

3. **`H2_Moderation_SDT_Acceptance.ipynb`**
   - H2a: Role moderation (Combined China+USA sample)
   - H2b: Role moderation (USA-only 3-level analysis)
   - Results: No significant moderation (all ΔR²<0.005)

4. **`H3_Cross_Cultural_Moderation.ipynb`**
   - H3: Country moderation × 3 technologies
   - Simple slopes analysis by country
   - Results: Strong cross-cultural moderation (all p<0.001)

### Data Structure
```
data/
├── china/          # Chinese survey data (CN_all.csv, CN_client.csv, CN_therapist.csv)
├── usa/            # US survey data (USA_all.csv)
├── merged/         # Harmonized datasets
└── output/         # Analysis-ready data (processed_for_analysis.csv)
```

**Note**: Data files are excluded from git via `.gitignore` for privacy.

---

## Research Hypotheses (Revised Framework)

### H1: Main Effects of Self-Determination
> *"Self-determination predicts attitudes towards AI for 3 mental health technologies (Avatar, Chatbot, Teletherapy), while controlling for confounders (GAAIS, demographics, etc.)"*

**Status**: ✓ Partially supported - Technology-specific patterns

### H2: Clinical Role Moderation
> *"Clinical role moderates this relationship × 3 technologies"*

Two analyses:
- **H2a**: Combined China+USA (Clinician vs Patient)
- **H2b**: USA only (Clinician vs Patient vs Community)

**Status**: ✗ Not supported - Negligible effects (ΔR²<0.005)

### H3: Cross-Cultural Moderation
> *"Country moderates this relationship × 3 technologies"*

**Status**: ✓✓✓ Strongly supported - All p<0.001, consistent across technologies

---

## Key Variables

### Predictor
- **TENS_Life_mean**: Self-Determination Theory (basic psychological needs: autonomy, competence, relatedness)

### Outcomes (Three Separate Measures)
- **Accept_avatar**: AI avatar / generic AI therapist acceptance
- **Accept_chatbot**: AI chatbot acceptance
- **Accept_tele**: Teletherapy / human therapist acceptance

### Control Variables (NOT Moderators)
- **GAAIS_mean**: General AI attitudes (covariate)
- **ET_mean**: Epistemic trust (covariate)
- **PHQ5_mean**: Depressive symptoms
- **SSRPH_mean**: Mental health stigma
- **age**: Continuous
- **gender**: Categorical

### Moderators
- **Country**: China (0) vs USA (1)
- **role_binary**: Clinician (0) vs Patient (1) [for combined analysis]
- **role_label_usa3**: Clinician / Patient / Community [for USA-only analysis]

---

## Sample Characteristics

| Sample | N (Raw) | N (After Imputation) | Age M(SD) | % Female |
|--------|---------|---------------------|-----------|----------|
| China | 485 | 485 | 32.4 (10.2) | 58% |
| USA | 1857 | 1742 | 38.7 (13.5) | 72% |
| **Total** | 2342 | **2227** | 37.1 (12.8) | 68% |

**Sample retention**: 95.1% after multiple imputation (MICE algorithm)

---

## Setup & Usage

### Installation
```bash
# Install required packages
pip install -r requirements.txt
```

### Running Analyses
```bash
# 1. Data preparation
jupyter notebook Exploratory_Data_Analysis.ipynb

# 2. Hypothesis testing (can run in any order after step 1)
jupyter notebook H1_Main_Effect_SDT_Acceptance.ipynb
jupyter notebook H2_Moderation_SDT_Acceptance.ipynb
jupyter notebook H3_Cross_Cultural_Moderation.ipynb
```

### Key Outputs
- **Analysis-ready data**: `data/output/processed_for_analysis.csv`
- **Completion summaries**: Added to end of each notebook
- **Comprehensive report**: `COMPREHENSIVE_ANALYSIS_REPORT.md`

---

## Methodological Notes

### Design
- Cross-sectional survey design
- Convenience sampling (clinicians, patients, community members)
- Cross-cultural comparison (China vs USA)

### Analytic Strategy
1. **Confounder-first approach**: Test confounders before adding predictors
2. **Technology-specific models**: Each of 3 technologies analyzed separately
3. **Hierarchical regression**: Baseline → Main effect → Moderation
4. **Effect size reporting**: Standardized β, ΔR², Cohen's f²

### Data Quality
- ✓ All scales show good reliability (α>0.70)
- ✓ Multiple imputation for missing data (MICE)
- ✓ Multicollinearity checked (all VIF<2.0)
- ✓ Sample size adequate for all analyses

---

## Results Summary

### H1: Main Effects
| Technology | β (SDT) | p-value | Interpretation |
|------------|---------|---------|----------------|
| Avatar | 0.008 | 0.635 | No relationship |
| Chatbot | 0.048 | 0.006** | Small positive |
| Teletherapy | -0.132 | <0.001*** | Moderate negative |

**Conclusion**: SDT effects vary by technology type (not universal)

### H2: Role Moderation
| Analysis | ΔR² Range | Typical p | Conclusion |
|----------|-----------|-----------|------------|
| H2a (Combined) | <0.005 | p>0.10 | No moderation |
| H2b (USA-only) | <0.005 | p>0.10 | No moderation |

**Conclusion**: Clinical role does NOT moderate SDT-acceptance relationships

### H3: Country Moderation
| Technology | β (Interaction) | p-value | ΔR² | Conclusion |
|------------|-----------------|---------|------|------------|
| Avatar | -0.334 | <0.001*** | 0.023 | Strong moderation |
| Chatbot | -0.258 | <0.001*** | 0.013 | Strong moderation |
| Teletherapy | -0.291 | <0.001*** | 0.011 | Strong moderation |

**Conclusion**: Country STRONGLY moderates all SDT-acceptance relationships

**Pattern**: SDT effects more positive in China than USA across all technologies

---

## Next Steps

### For Manuscript
- [ ] Draft Results section (H1, H2, H3 integrated)
- [ ] Create interaction plots for H3 (primary finding)
- [ ] Draft Discussion emphasizing cultural context
- [ ] Prepare supplementary tables

### Potential Follow-Ups
- Test specific cultural dimensions (Hofstede indices)
- Qualitative interviews to understand mechanisms
- Longitudinal design with actual technology use
- Expand to additional countries

---

## Citation & Acknowledgments

**Recommended Citation** (pre-publication):
> Zhao, J., & Aafjes-van Doorn, K. (2024). *Predicting AI acceptance in mental health interventions through self-determination theory: A cross-cultural study*. Manuscript in preparation.

**Affiliation**:
- Katie Aafjes-van Doorn, PhD - NYU Shanghai, Associate Professor in Psychology
- Jackson Zhao - Columbia University

**Potential Presentation**:
- Society for Psychotherapy Research (SPR) 2026 Conference, Osaka, Japan

---

## Software & Dependencies

- **Python**: 3.11+
- **Key packages**: pandas, numpy, statsmodels, scikit-learn, matplotlib, seaborn
- **Environment**: Jupyter Notebook
- **Version control**: Git

See `requirements.txt` for complete package list with versions.

---

## Project Timeline

- **Nov 2024**: Initial analyses completed
- **Dec 1-9, 2024**: Framework revision per Katie's specifications
- **Dec 11, 2024**: All analyses finalized, documentation complete
- **Dec 12, 2024**: Meeting with Katie to review results
- **Next**: Manuscript preparation

---

## Contact

**For inquiries about this research**:
- Katie Aafjes-van Doorn: kav9239@nyu.edu
- Jackson Zhao: zz3119@columbia.edu

**Project Status**: ✅ Analysis complete, ready for manuscript preparation

---

*Last updated: December 11, 2024*
